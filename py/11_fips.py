import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff


def call_file(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df


path1 = '/Users/nathanoliver/Desktop/Cancer Rates/csv/07_fips/US_FIPS_Codes.csv'

df = call_file(path1)

print(df.columns)

df['fips'] = 0

for i in range(len(df)):
    if df.loc[i, 'fips_state'] < 10:
        df.loc[i, 'fips_state'] = '0' + str(df.loc[i, 'fips_state'])
        print(df.loc[i, 'fips_state'])
    else:
        df.loc[i, 'fips_state'] = str(df.loc[i, 'fips_state'])

for i in range(len(df)):
    if df.loc[i, 'fips_county'] < 10:
        df.loc[i, 'fips_county'] = '00' + str(df.loc[i, 'fips_county'])
        print(df.loc[i, 'fips_county'])
    elif df.loc[i, 'fips_county'] >= 10 and df.loc[i, 'fips_county'] < 100:
        df.loc[i, 'fips_county'] = '0' + str(df.loc[i, 'fips_county'])
        print(df.loc[i, 'fips_county'])
    else:
        df.loc[i, 'fips_county'] = str(df.loc[i, 'fips_county'])


for i in range(len(df)):
    df.loc[i, 'fips'] = df.loc[i, 'fips_state'] + df.loc[i, 'fips_county']
    df.loc[i, 'fips'] = str(df.loc[i, 'fips'])

# df['fips'] = df['fips_state'] + df['fips_county']

print(df)

df['fips'] = df['fips'].astype('str')

df.to_excel(
    '/Users/nathanoliver/Desktop/Cancer Rates/csv/07_fips/fips.xlsx',  index=False)
