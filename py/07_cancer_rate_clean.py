import pandas as pd

path = '/Users/nathanoliver/Desktop/Cancer Rates/csv/06_csv_cancer_rates/cancer_rates02.csv'
data = pd.read_csv(path)
df = pd.DataFrame(data)

print(df.columns)

df = df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis='columns')

print(df.columns)

print(df['incidence_rate'].describe())

cols = ['incidence_rate', 'lower_95%', 'upper_95%', 'average_annual_count']


for col in cols:
    df = df[df[col] != '�']
    df = df[df[col] != '��']
    df = df[df[col] != '���']
    df = df[df[col] != '*']
    df = df[df[col] != '**']
    df = df[df[col] != '***']
    df[col] = pd.to_numeric(df[col])
    print(df[col].describe())

df.to_csv('/Users/nathanoliver/Desktop/Cancer Rates/csv/06_csv_cancer_rates/cancer_rates_drop_cells.csv')
