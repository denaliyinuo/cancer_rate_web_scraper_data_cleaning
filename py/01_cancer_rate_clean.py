import csv
import openpyxl

for i in range(1, 2121):

    FromPath = '/Users/nathanoliver/Desktop/Cancer Rates/csv/01_csv_original/incd-' + \
        str(i) + '.csv'
    ToPath = '/Users/nathanoliver/Desktop/Cancer Rates//xlsx/02_xlsx/incd-' + \
        str(i) + '.xlsx'

    wb = openpyxl.Workbook()
    ws = wb.active

    with open(FromPath) as f:
        reader = csv.reader(f, delimiter=':')
        for row in reader:
            ws.append(row)

    wb.save(ToPath)
