import json
import pandas as pd


tmp = pd.read_csv("pharmacy_ga.csv")
tmp.zipcode = tmp.zipcode.astype(int)

tmp_gp = tmp[tmp.source == 'gp']
agg_gp = tmp_gp.groupby(by=["zipcode"]).count()
agg_json = agg_gp.to_dict()

with open("zipdata.json", "w") as outfile:
    outfile.write(json.dumps(agg_json["census"]))