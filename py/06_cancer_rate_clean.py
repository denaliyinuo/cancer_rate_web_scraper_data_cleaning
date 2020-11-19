import pandas as pd


path = '/Users/nathanoliver/Desktop/Cancer Rates/csv/06_csv_cancer_rates/cancer_rates_original.csv'
data = pd.read_csv(path)
df = pd.DataFrame(data)

print(len(df))

print(df.columns)

df = df[df.incidence_rate != '*']

print(len(df))

col = ['incidence_rate', 'lower_95%', 'upper_95%', 'average_annual_count']


df.to_csv('/Users/nathanoliver/Desktop/Cancer Rates/csv/06_csv_cancer_rates/cancer_rates02.csv')
