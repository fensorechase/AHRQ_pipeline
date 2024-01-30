import json
import pandas as pd

"""
This script writes a json file with zip codes (key) and the number of pharmacies in that zip code (value).
Adjust code to filter for 'source': either 'gp' or 'fsq' 
"""

# Read df in
tmp = pd.read_csv("../Data/GA_Pharmacy_Data_gp_fsq/pharmacy_ga.csv")

# Drop rows where zipcode is None
tmp = tmp.dropna(subset=['zipcode'])
tmp = tmp.reset_index(drop=True)

# Cast zipcode to int
tmp.zipcode = tmp.zipcode.astype(int)

# To select pharmacies from Google Places: 'gp'
# To select pharmacies from Foursquare: 'fsq'
# To use pharmacies from both data sources, delete the line used to filter 'source'.
tmp_gp = tmp[tmp.source == 'fsq']

# Count number of pharmacies per zipcode
agg_gp = tmp_gp.groupby(by=["zipcode"]).count()
agg_json = agg_gp.to_dict()

# Write to json -- 'census' column is arbitrary, used to write dict keys, values at 'zipcode' level.
with open("fsq_zipdata.json", "w") as outfile:
    outfile.write(json.dumps(agg_json["census"]))