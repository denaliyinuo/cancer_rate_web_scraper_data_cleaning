from selenium import webdriver
# from openpyxl import load_workbook
# import bs4
# import requests as re

# https://www.statecancerprofiles.cancer.gov/incidencerates/


browser = webdriver.Safari()

# all ages, races, sexes

cancers = ['071', '076', '020', '017', '072', '090',
           '035', '047', '053', '086', '003', '040', '018', '080']
races = ['01', '02', '03', '04', '05', '06', '07']
sexes = ['1', '2']
ages = ['009', '136', '006', '157']

for cancer in cancers:
    for race in races:
        for sex in sexes:
            for age in ages:

                website = 'https://www.statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=00&areatype=county' + '&cancer=' + \
                    str(cancer) + '&race=' + str(race) + '&sex=' + str(sex) + '&age=' + str(age) + \
                    '&stage=999&year=0&type=incd&sortVariableName=rate&sortOrder=desc&output=1'

                browser.get(website)

# female only

female_cancers = ['055', '400', '057', '061', '058']

for cancer in female_cancers:
    for race in races:
        for age in ages:

            website = 'https://www.statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=00&areatype=county' + '&cancer=' + \
                str(cancer) + '&race=' + str(race) + '&age=' + str(age) + \
                '&stage=999&year=0&type=incd&sortVariableName=rate&sortOrder=desc&output=1'

            browser.get(website)

# male only

male_cancers = ['066']

for cancer in male_cancers:
    for race in races:
        for age in ages:

            website = 'https://www.statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=00&areatype=county' + '&cancer=' + \
                str(cancer) + '&race=' + str(race) + '&age=' + str(age) + \
                '&stage=999&year=0&type=incd&sortVariableName=rate&sortOrder=desc&output=1'

            browser.get(website)

# children only

child_cancers = ['516', '515']

for cancer in child_cancers:
    for race in races:
        for age in ages:

            website = 'https://www.statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=00&areatype=county' + '&cancer=' + \
                str(cancer) + '&race=' + str(race) + '&sex=' + str(sex) + \
                '&stage=999&year=0&type=incd&sortVariableName=rate&sortOrder=desc&output=1'

            browser.get(website)
