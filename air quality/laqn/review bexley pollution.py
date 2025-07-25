import os
import pandas as pd
import glob

os.chdir(r"C:\Users\dimit\Downloads\bexley air quality")

dfs = []
for file in glob.glob("laqn*.csv"):
    df = pd.read_csv(file, parse_dates = ["ReadingDateTime"])
    df.columns = [s.lower() for s in df.columns]
    df = df.rename(columns = {"readingdatetime": "date", "species": "pollutant"})
    df = df.loc[~pd.isnull(df.value)]
    dfs.append(df)

df = pd.concat(dfs)

m = {"BX2": "Belvedere",
     "BQ7": "Belvedere West",
     "BQ9": "Slade Green",
     "BX1": "Slade Green",
     "BX9": "Slade Green",
     "GN4": "Fiveways Sidcup A20",
     "GB6": "Falconwood",
     "GB0": "Falconwood"}

df["location"] = df.site.apply(lambda s: m[s])

dg = pd.read_csv("bexley air pollution measurement locations.csv")

dh = pd.merge(df, dg, on = "location", how = "left") 

dh.to_csv("bexley air pollution.csv", index = False)
