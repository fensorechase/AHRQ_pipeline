# AHRQ_pipeline

Key Steps
Load Libraries:

caret
data.table
dplyr
sets
scales
tidyr
stringr
Load Data:

Load patient data from a CSV file.
Load multiple years of AHRQ SDOH data from CSV files.
Load a CSV file containing feature names for AHRQ SDOH variables.
Preprocess AHRQ Data:

Merge AHRQ data from multiple years into a single data frame.
Pad ZIP codes and STATEFIPS codes with leading zeros for consistency.
Optionally perform imputation for missing values.
Merge Data:

Merge the preprocessed AHRQ data with patient data using crosswalk variables:
STATEFIPS
ZIPCODE
YEAR
Write Output:

Write the merged data to a CSV file.
Additional Information
The notebook includes code for data summarization and visualization using bar charts.
Potential areas for further work include:
Implementing imputation strategies.
Exploring different merging approaches.
Conducting further analysis on the merged data.
For more details and the full code, please refer to the notebook itself.

The AHRQ SDOHD data used in this notebook can be accessed from the following link:

AHRQ SDOHD: https://www.ahrq.gov/sdoh/data-analytics/sdoh-data.html#download

