import os
import pandas as pd

PATH = r"C:\Users\dimit\Documents\GitHub\bexley\budget"
os.chdir(PATH)

x = pd.read_csv("borough population 2021.csv").rename(columns = {"category": "borough_category"})

y = pd.read_csv("social care grant 2024-25.csv")
z = pd.melt(y, id_vars = "borough")


j = z.variable.isin(["Total Revenue Grants Within AEF", 
                     "Total Revenue Grants Outside AEF",
                     "Total Specific And Special Revenue Grants"])
z = z.loc[~j]

z1 = z.copy()
w1 = pd.merge(z1, x[["borough", "borough_category"]], how = "left", on = "borough").assign(is_per_capita = 0)

z2 = z.copy()
w2 = pd.merge(z2, x, how = "left", on = "borough").assign(is_per_capita = 1)
w2["value"] = 1000*w2.value/w2.population_2021
w2["variable"] = w2["variable"] + " - per capita"
del w2['population_2021']

w = pd.concat([w1, w2])

w = w.loc[w.borough != "City of London"]

w.to_csv("OUTPUT grant.csv", index = False)