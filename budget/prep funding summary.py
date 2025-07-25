import os
import pandas as pd

PATH = r"C:\Users\dimit\Documents\GitHub\bexley\budget"
os.chdir(PATH)

x = pd.read_csv("OUTPUT budget detailed.csv")

m = {"REVENUE EXPENDITURE - per capita": "Revenue Expenditure",
     "Specific and special grants inside AEF [SG line 699 as income] - per capita": "Grants",
     "Appropriations to(+)/ from(-) schools' reserves - per capita": "Reserves Change",
     "Appropriations to(+)/ from(-) dedicated schools grant reserves - per capita": "Reserves Change",
     "Appropriations to(+)/ from(-) public health financial reserves - per capita": "Reserves Change",
     "Appropriations to(+)/ from(-) other earmarked financial reserves - per capita": "Reserves Change",
     "Appropriations to(+)/ from(-) unallocated financial reserves - per capita": "Reserves Change",
     "Revenue Support Grant - per capita": "Revenue Support Grant",
     "Retained income from Rate Retention Scheme ** - per capita": "Business Rates",
     "Collection fund surpluses and deficits for Council Tax - per capita": "Other",
     "Other Items - per capita": "Other",
     "COUNCIL TAX REQUIREMENT (total of lines 900 to 985) - per capita": "Council Tax Requirement"}

j = x.variable.isin(list(m.keys())) 
x = x.loc[j]

x["item"] = x.variable.map(m)

g = x.groupby(['borough', 'borough_category', 'is_per_capita', 'item'])["value"].sum().reset_index()
g = g.rename(columns = {"item": "variable"})

j = g.variable.isin(["Revenue Expenditure", "Council Tax Requirement"])
g.value[~j] = - g.value[~j]

g.to_csv("OUTPUT funding summary.csv", index = False)


