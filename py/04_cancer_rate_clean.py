import pandas as pd

for i in range(1, 1009):
    print(i)
    filename = '/Users/nathanoliver/Python/Cancer Rates/xlsx/04_xlsx_final/incd-' + \
        str(i) + '-final.xlsx'

    csv = '/Users/nathanoliver/Python/Cancer Rates/csv/05_csv_final/incd-' + \
        str(i) + '-final.csv'

    df = pd.read_excel(filename)
    df.to_csv(csv, index=False)
