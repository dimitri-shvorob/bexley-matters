import pandas as pd
import os

os.chdir(r"C:\Users\dimit\Documents\My Projects\bexley-road-safety\detailed data")
         
x = pd.read_csv("bexley collision.csv", low_memory = False)
x["accident_index"] = x.accident_index.astype(str)

y = pd.read_csv("pedestrian casualty.csv", low_memory = False)

# is accident index unique across years? yes
len(set(x.accident_index))

z = pd.merge(x, y,  on = "accident_index", how = "inner")
z["accident_index"] = "a" + z.accident_index 

z.to_csv("bexley pedestrian casualty.csv", index = False) 

# select one casualty per collisoon

z = z.sort_values(by = ["accident_index", "casualty_severity"], ascending = False)

w = z.drop_duplicates(subset = ["accident_index"])

z.to_csv("bexley collision with pedestrian casualty.csv", index = False) 

