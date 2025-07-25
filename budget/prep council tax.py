import os
import pandas as pd

PATH = r"C:\Users\dimit\Documents\GitHub\bexley\budget"
os.chdir(PATH)

x = pd.read_csv("borough population 2021.csv").rename(columns = {"category": "borough_category"})
y = pd.read_csv("borough council tax 2024-25.csv")
z = pd.merge(y, x, on = "borough")
del z["population_2021"]

z = z.loc[z.borough != "City of London"]

z.to_csv("OUTPUT council tax.csv")