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

## Summary of functionality: 

### Load Data:
- Load patient data from a CSV file. (select your desired geographic level & years from AHRQ SDOHD).
- Load years of AHRQ SDOH data from CSV files.
- Load a CSV file containing feature names for AHRQ SDOH variables.

### Preprocess AHRQ Data:
- Merge AHRQ data from multiple years into a single data frame.
- Pad ZIP codes and STATEFIPS codes with leading zeros for consistency.
- Optionally perform imputation for missing values.

### Merge Data:
Merge the preprocessed AHRQ data with patient data using crosswalk variables:
STATEFIPS
ZIPCODE
YEAR

## The AHRQ SDOHD data used in this notebook can be accessed from the following link:
- AHRQ SDOHD: https://www.ahrq.gov/sdoh/data-analytics/sdoh-data.html#download

