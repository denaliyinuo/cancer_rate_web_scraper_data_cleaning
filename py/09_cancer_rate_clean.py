import pandas as pd
import numpy as np


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


path1 = '/Users/nathanoliver/Desktop/Python/Cancer Rates/06_csv_cancer_rates/cancer_rates.csv'
path2 = '/Users/nathanoliver/Desktop/Python/Cancer Rates/06_csv_cancer_rates/ctyfactbook2019.csv'

df_can = call_file(path1)
df_air = call_file(path2)

print(df_can.columns)
print(df_air.columns)

# df_air['county_state'] =

df_air['county_state'] = df_air['County'] + ', ' + df_air['State']
df_can['county_state'] = df_can['county'] + ', ' + df_can['state']

df_air.set_index('county_state', inplace=True)
df_can.set_index('county_state', inplace=True)

print(df_air.head())
print(df_can.head())

df_air.replace(['ND', 'IN'], '', inplace=True)
df_can.replace(np.nan, '', inplace=True)


print(df_air.head())
print(df_can.head())

print('air length:    ', len(df_air))
print('cancer length: ', len(df_can))

# df_can.set_index('county_state')
# print(df_can.head())

# df = pd.concat([df_air, df_can], axis=1, join='inner')

# df.to_csv('/Users/nathanoliver/Desktop/Python/Cancer Rates/06_csv_cancer_rates/individual_cancer_air_data.csv')

# print('df length:     ', len(df))

