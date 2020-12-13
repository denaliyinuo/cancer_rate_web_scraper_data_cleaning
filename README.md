# US Cancer Rate Data Collection and Cleaning

US cancer rates for different cancers broken down by county, age group, gender, and ethnicity

# Overview

I created a web scraper to gather cancer incidence rates in the US for different cancers broken down by county, age group, gender, and ethnicity.  I further cleaned the data to remove null values and collate over 1000 files into a single csv file for analysis.

Workflow Steps


1. Python program calls URLs using Selenium from the National Cancer Institute (NCI) website.
2. Each URL automatically downloads a CSV file containing cancer incidence rates.
3. CSV files are converted into XLSX files.  Pandas cannot be used in this instance, therefore Openpxyl is used.
4. XLSX files are cleaned using Openpyxl.
5. XLSX files are converted back into CSVs.
6. CSVs are merged into single CSV file.

![image 2](/images/image2.png)

# Data

The resulting [CSV file](https://raw.githubusercontent.com/denaliyinuo/cancer_rate_web_scraper_data_cleaning/main/csv/06_csv_cancer_rates/cancer_rates.csv) has over 100,000 data points, broken down by county, age group, gender, and ethnicity.  Below is a snapshot of the data.

![image 4](/images/image4.png)

# Results

![image 5](/images/image5.png)
