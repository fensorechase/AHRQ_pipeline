# Quick Start -- Working with Social Determinants of Health (SDOH) Data at the 'Area Level'

This is starter repository for working with area-level social determinants of health (SDOH) data fom the US Agency for Healthcare Research and Quality (AHRQ). Here, you will find basic examples on how to merge and pre-process the area-level SDOH data for downstream tasks.


## Background

- What are SDOH?
>> SDOH are the non-medical factors that influence health outcomes. They're the conditions in which people are born, grow, work, live, and age that affect their health, functioning, and quality of life. More recently, they have also been referred to as social drivers of health.
- What does 'area-level' SDOH mean?
>> Area-level SDOH are SDOH that exist at a community or geographic level rather than at an individual person's level. These are characteristics of neighborhoods, regions, or communities that affect the health of people living in those areas. For example, while an individual's income may be a personal SDOH, neighborhood poverty rate would be an area-level SDOH (neighborhood may refer to ZIP code level, census tract level, etc.).

## Quickstart

- Clone this repository with ```git clone https://github.com/fensorechase/AHRQ_pipeline.git```

- The Social Determinants of Health Dataset (SDOHD) from AHRQ is available for free download at [https://www.ahrq.gov/sdoh/data-analytics/sdoh-data.html#download](https://www.ahrq.gov/sdoh/data-analytics/sdoh-data.html#download) -- or if you have been given access to the Emory University OneDrive with the AHRQ SDOHD raw csv data, you should use that. 

## Folder Structure
- After downloading Data folder from specified OneDrive:
```
.
├── AHRQ_pipeline
│   ├── compress_pharma.py
│   ├── merge_AHRQ.Rmd
│   ├── gp_zipdata.json
│   └── fsq_zipdata.json
└── Data: download from OneDrive
    ├── AHRQ
    │   ├── COUNTY
    │   ├── TRACT
    │   └── ZIP
    ├── fake_patient_data.csv
    └── GA_Pharmacy_Data_gp_fsq
```

## Summary of Functionality: 
1. merge_AHRQ.Rmd: reads all available years of AHRQ SDOH data at ZIP code level. Generates summary plots, and includes template to merge SODH with patient data by ZIP code, year.
2. compress_pharma.py: reads Georgia pharmacy locations, and generates summary statistics by writing a json file with zip codes (key) and the number of pharmacies in that zip code (value).

### Merge Data: recommended approaches for merging this SDOH data with patient data.
Merge the preprocessed AHRQ data with patient data using crosswalk variables:
- STATEFIPS
- ZIPCODE
- YEAR
Merge the Georgia pharmacy location data with patient data using crosswalk variables:
- zipcode
- can optionally select either 'gp' or 'fsq' as the data source for Georgia pharmacy location data (see gp_zipdata.json, fsq_zipdata.json), or use both sources combined (

## The raw AHRQ SDOHD data used in this notebook can be accessed from the following link:
- AHRQ SDOHD: https://www.ahrq.gov/sdoh/data-analytics/sdoh-data.html#download
(If you have access, we recommend using the OneDrive ZIP code level data because we have already isolated relevant sheets from the csv files at the above link)

## Libraries/Packages
(R workspace) Load Libraries:
- caret
- data.table
- dplyr
- sets
- scales
- tidyr
- stringr

(Python workspace) Load packages:
- json
- pandas

## Disclaimer

This repository is not affiliated with the Agency for Healthcare Research and Quality (AHRQ) -- it is intended only for general purpose 
