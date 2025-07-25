import pandas as pd
import os
import glob

os.chdir(r"C:\Users\dimit\Documents\My Projects\bexley-road-safety\detailed data")
         
dfs = []
ff = glob.glob(r"C:\Users\dimit\Documents\My Projects\bexley-road-safety\detailed data\*casualty-20*")

for f in ff:
    df = pd.read_csv(f, low_memory = False)
    j = df.casualty_class == 3
    df = df.loc[j]
    dfs.append(df)
    
df = pd.concat(dfs)
df.to_csv("pedestrian casualty.csv", index = False)

