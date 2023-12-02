import pandas as pd


def print_(a=''):
    print('~' * 80, '\n', a, '\n')


pd.set_option('display.max_columns', None)

url = "https://en.wikipedia.org/wiki/List_of_minor_planets:_1%E2%80%931000"

tables = pd.read_html(url)

sel_tables = tables[1:-1]

df = pd.concat(sel_tables, ignore_index=True)

df.columns = [i[1] for i in df.columns]
print(df.columns)
print_('Header renamed')
print(df)  # (b) correct

df.drop(columns=['Provisional', 'Category', 'Ref'], axis=1)
print_('“Provisional”, “Category”, “Ref” deleted')
print(df)  # (c) correct

top_cities = df['Site'].value_counts()
print_('Top cities')
print(top_cities.head(3))

df['Diam.'] = [float(i.split()[0]) for i in df['Diam.']]

small_pl = df[df['Diam.'] < 15]
medium_pl = df[(df['Diam.'] >= 50) & (df['Diam.'] <= 200)]
big_pl = df[df['Diam.'] > 500]

print_('Planets by size category')
print("Small planets (up to 15 km)\n")
print(small_pl)

print("\nMedium planets (from 50 to 200 km)\n")
print(medium_pl)

print("\nBig planets (more than 500 km)\n")
print(big_pl)
