# AHRQ_pipeline

## Key Steps
Load Libraries:
- caret
- data.table
- dplyr
- sets
- scales
- tidyr
- stringr


## Folder Structure
- After downloading Data folder from specified OneDrive:
```
.
├── AHRQ_pipeline
│   ├── compress_pharma.py
│   ├── merge_AHRQ.Rmd
│   ├── gp_zipdata.json
│   └── fsq_zipdata.json
└── Data: _download from OneDrive_
    ├── AHRQ
    │   ├── COUNTY
    │   ├── TRACT
    │   └── ZIP
    └── GA_Pharmacy_Data_gp_fsq
```

## Summary of functionality: 
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

## The AHRQ SDOHD data used in this notebook can be accessed from the following link:
- AHRQ SDOHD: https://www.ahrq.gov/sdoh/data-analytics/sdoh-data.html#download

