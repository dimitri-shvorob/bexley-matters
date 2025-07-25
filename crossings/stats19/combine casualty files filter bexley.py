import pandas as pd
import os
import glob

os.chdir(r"C:\Users\dimit\Documents\My Projects\bexley-road-safety\detailed data")
         
dfs = []
ff = glob.glob(r"C:\Users\dimit\Documents\My Projects\bexley-road-safety\detailed data\*accident-20*")

for f in ff:
    df = pd.read_csv(f, low_memory = False)
    j = df.local_authority_ons_district == "E09000004"
    df = df.loc[j]
    dfs.append(df)
    
df = pd.concat(dfs)
df.to_csv("bexley collision.csv", index = False)

