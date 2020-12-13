import pandas as pd

path = '/Users/nathanoliver/Desktop/Cancer Rates/csv/06_csv_cancer_rates/cancer_rates_drop_cells.csv'
data = pd.read_csv(path)
df = pd.DataFrame(data)

cat_col = ['cancer']

for col in cat_col:
    print(df[col].unique())

['Bladder (All Stages^)' 'Brain & ONS (All Stages^)'
 'Colon & Rectum (All Stages^)' 'Esophagus (All Stages^)'
 'Kidney & Renal Pelvis (All Stages^)' 'Leukemia (All Stages^)'
 'Liver & Bile Duct (All Stages^)' 'Lung & Bronchus (All Stages^)'
 'Melanoma of the Skin (All Stages^)' 'Non-Hodgkin Lymphoma (All Stages^)'
 'Oral Cavity & Pharynx (All Stages^)' 'Pancreas (All Stages^)'
 'Stomach (All Stages^)' 'Thyroid (All Stages^)' 'Breast (All Stages^)'
 'Breast (in situ) (All Stages^)' 'Cervix (All Stages^)'
 'Ovary (All Stages^)' 'Uterus (Corpus & Uterus' 'Prostate (All Stages^)'
 'Childhood - Ages <15' 'Childhood - Ages <20']
['White (includes Hispanic)' 'Black (includes Hispanic)'
 'Amer. Indian/Alaskan Native (includes Hispanic)'
 'Asian or Pacific Islander (includes Hispanic)' 'Hispanic (any race)'
 'White Hispanic' 'White Non-Hispanic']
['Male' 'Female']
['Ages <50' 'Ages 50+' 'Ages <65' 'Ages 65+' '<15' '<20']


def replace(str1, str2):
    return df.replace(str1, str2)


for string in df.cancer.unique():
    string = str(string.strip())
    rep = ' (All Stages^)'

    new_string = string[:-14]

    if rep in string:
        df = replace(string, new_string)
    else:
        pass

['White (includes Hispanic)' 'Black (includes Hispanic)'
 'Amer. Indian/Alaskan Native (includes Hispanic)'
 'Asian or Pacific Islander (includes Hispanic)' 'Hispanic (any race)'
 'White Hispanic' 'White Non-Hispanic']


for string in df.race.unique():
    string = str(string.strip())
    print(string)
    rep = ' (includes Hispanic)'

    new_string = string[:-20]

    if rep in string:
        df = replace(string, new_string)
    else:
        pass

df = replace('Hispanic (any race)', 'Hispanic')
df = replace('Uterus (Corpus & Uterus', 'Uterus')

# df = replace('Bladder (All Stages^)', 'Bladder')


for string in df.age.unique():
    string = str(string.strip())
    print(string)
    rep = 'Ages '

    new_string = string[4:]

    if rep in string:
        df = replace(string, new_string)
    else:
        pass

cat_col = ['cancer', 'race', 'sex', 'age']

for col in cat_col:
    print(df[col].unique())

df = replace('District of Columbia(6', 'District of Columbia')
df = replace('8)', 'District of Columbia')

df = replace(' <50', '<50')
df = replace(' <65', '<65')
df = replace(' 50+', '50+')
df = replace(' 65+', '65+')


['Ages <50' 'Ages 50+' 'Ages <65' 'Ages 65+' '<15' '<20']


df = df.drop(columns='Unnamed: 0', axis='columns')

print(df.columns)


df.to_csv('/Users/nathanoliver/Desktop/Cancer Rates/csv/06_csv_cancer_rates/cancer_rates.csv')
