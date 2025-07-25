import os
import pandas as pd

PATH = r"C:\Users\dimit\Documents\GitHub\bexley\schools"
os.chdir(PATH)

x = pd.read_csv("school.csv")
y = pd.read_csv("bexley selection test.csv", )

z = pd.merge(y, x, how = "left", on = "name", indicator = True)

z = z.rename(columns = {"leaver_class_size_2023": "number_pupils"})

z["min_number_selective"] = z.number_selective.fillna(0)
z["max_number_selective"] = z.number_selective.fillna(5)
	
z["min_selective_rate_vs_takers"] = z.min_number_selective/z.number_takers	
z["max_selective_rate_vs_takers"] = z.max_number_selective/z.number_takers	

z["min_selective_rate_vs_class_size"] = z.min_number_selective/z.number_pupils	
z["max_selective_rate_vs_class_size"] = z.max_number_selective/z.number_pupils	

z.to_csv("OUTPUT bexley selection test by year.csv", index = False)

# across years
zr = z[["name", "latitude", "longitude", "min_number_selective", "max_number_selective", "number_takers", "number_pupils"]]
zg = zr.groupby(["name"]).agg({"latitude": "min",
                               "longitude": "min", 
                               "min_number_selective": "sum",
                               "max_number_selective": "sum",
                               "number_takers": "sum",
                               "number_pupils": "sum"}).reset_index()

zg["min_selective_rate_vs_takers"] = zg.min_number_selective/zg.number_takers	
zg["max_selective_rate_vs_takers"] = zg.max_number_selective/zg.number_takers	

zg["min_selective_rate_vs_class_size"] = zg.min_number_selective/zg.number_pupils	
zg["max_selective_rate_vs_class_size"] = zg.max_number_selective/zg.number_pupils	

zg.to_csv("OUTPUT bexley selection test across years.csv", index = False)


