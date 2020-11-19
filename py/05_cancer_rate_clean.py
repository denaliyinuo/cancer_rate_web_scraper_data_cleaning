import pandas as pd

i = 1
j = 2


def call_file(i):
    path = '/Users/nathanoliver/Desktop/Cancer Rates/csv/05_csv_final/incd-' + \
        str(i) + '-final.csv'
    data = pd.read_csv(path)
    return pd.DataFrame(data)


def concat(df1, df2):
    return pd.concat((df1, df2), axis='index')


df1 = call_file(1)
df2 = call_file(2)

print(len(df1))
print(len(df2))

df = pd.concat((df1, df2), axis='index')

for i in range(3, 1009):
    df2 = call_file(i)
    df = concat(df, df2)
    print(i)

df.to_csv('/Users/nathanoliver/Desktop/Cancer Rates/csv/06_csv_cancer_rates/cancer_rates_original.csv')
