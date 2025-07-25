import os
import pandas as pd
import numpy as np

PATH = r"C:\Users\dimit\Documents\GitHub\bexley\budget"
os.chdir(PATH)

x = pd.read_csv("OUTPUT budget detailed.csv")

# expenditure categories
m = {"TOTAL EDUCATION SERVICES - per capita": "Education",
     "TOTAL HIGHWAYS AND TRANSPORT SERVICES - per capita": "Highways",
     "TOTAL CHILDREN'S SOCIAL CARE - per capita": "Children's Social Care",
     "TOTAL ADULT SOCIAL CARE - per capita": "Adult Social Care",
     "TOTAL PUBLIC HEALTH - per capita": "Public Health",
     "TOTAL HOUSING SERVICES (GFRA only) - per capita": "Housing",
     "TOTAL CULTURAL AND RELATED SERVICES - per capita": "Culture",
     "TOTAL ENVIRONMENTAL AND REGULATORY SERVICES - per capita": "Environment",
     "TOTAL PLANNING AND DEVELOPMENT SERVICES - per capita": "Planning",
     "TOTAL POLICE SERVICES - per capita": "Police",
     "TOTAL FIRE AND RESCUE SERVICES - per capita": "Fire and Rescue",
     "TOTAL CENTRAL SERVICES - per capita": "Central Services",
     "TOTAL OTHER SERVICES - per capita": "Other"}

j = x.variable.isin(list(m.keys())) 
x1 = x.loc[j]
x1["expenditure_category"] = x1.variable.map(m)
del x1["variable"]
del x1["is_per_capita"]

xt = x.loc[x.variable == "TOTAL SERVICE EXPENDITURE - per capita", ["borough", "value"]].rename(columns = {"value": "value_total"})
xe = x1.loc[x1.expenditure_category == "Education", ["borough", "value"]].rename(columns = {"value": "value_education"})

y = pd.merge(x1, xt, on = "borough")
y = pd.merge(y, xe, on = "borough")

y["fraction_vs_total"] = y.value/y.value_total

y["fraction_vs_total_ex_education"] = y.apply(lambda row: np.nan if row.expenditure_category == "Education" else row.value/(row.value_total - row.value_education), axis = 1)

y.to_csv("OUTPUT spending summary.csv", index = False)


