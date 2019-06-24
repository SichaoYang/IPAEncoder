places = ['Bi­labial', 'Labio­dental', 'Linguo­labial', 'Dental', 'Alveolar', 'Post alveolar', 'Retro­flex', 'Alveolo-palatal', 'Palatal', 'Velar', 'Uvular', 'Pharyn­geal/epiglottal', 'Glottal']


def print_row(df):
    for p in places:
        for v in ['Unvoiced', 'Voiced']:
            l = df[(df[p] == 1) & (df[v] == 1)]['IPA'].to_numpy()
            assert len(l) < 2
            print(f'{(l[0] if len(l) == 1 else "_"):3}', end='')
    print()


import pandas as pd
df = pd.read_csv('consonants.csv')
# e.g. print_row(df[(df['Sibilant'] == 1) & (df['Fricative'] == 1)])
