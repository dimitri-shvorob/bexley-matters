import os
import pandas as pd

PATH = r"C:\Users\dimit\Documents\GitHub\bexley\budget"
os.chdir(PATH)

x = pd.read_csv("OUTPUT grant.csv")
j = x.borough.isin(["Bexley", "Bromley", "Greenwich"])
k = x.is_per_capita == 1
x = x.loc[j & k]
x = x.rename(columns = {"variable": "grant"})
x["grant"] = x.grant.apply(lambda s: s.replace(" - per capita", ""))

del x["borough_category"]
del x["is_per_capita"] 

xg = x.groupby("grant")["value"].max().reset_index()
xg["grant_category"] = xg.apply(lambda row: "Other" if row.value < 25 else row.grant, axis = 1) 

y = pd.merge(x, xg[["grant", "grant_category"]], on = "grant")

y.to_csv("OUTPUT grant triboro.csv", index = False)