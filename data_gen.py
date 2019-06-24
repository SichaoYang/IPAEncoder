__author__ = 'Sichao Yang'
__email__ = 'sichao@cs.wisc.edu'

import numpy as np
import pandas as pd
import re


class IPAEncoder:
    co_articulated = {}

    def __init__(self):
        self.df = pd.read_csv('csv/phonemes.csv')

    def encode(self, word, include_stress=True):
        word = re.sub(r'([A-Z])', lambda u: ' ' + u.group(0).lower(), word)
        sequence = []
        idx = 0
        while idx < len(word):
            matches = self.df[[word[idx:].startswith(i) for i in self.df.IPA]]
            if matches.empty:
                print(word)
            # assert not matches.empty, word
            matches = matches.loc[matches.IPA.map(len).idxmax()].to_numpy()
            sequence.append(matches[1:])
            idx += len(matches[0])
        return np.array(sequence, dtype=bool)


class WordEncoder:
    def __init__(self):
        import pandas
        vocab = pandas.read_csv('csv/phondict.csv')['ipa'].to_numpy()
        # np.random.shuffle(vocab)
        encoder = IPAEncoder()
        self.X = []
        t = 0
        T = 100
        for word in vocab:
            if t == T:
                print(t)
                T += 100
            t += 1
            self.X.append(encoder.encode(word))
        np.save('csv/encoded_words.npy', self.X)


if __name__ == '__main__':
    # unit test
    # encoder = IPAEncoder()
    # while True:
    #     print(encoder.encode(input()))
    WordEncoder()
