import os
import pandas as pd
from geopy.distance import geodesic

os.chdir(r"C:\Users\dimit\Documents\My Projects\bexley-road-safety")

x = pd.read_csv("bexley collision with pedestrian casualty reduced.csv", parse_dates = ["date"])
x["type"] = x.age_group_of_casualty.apply(lambda s: "Collision involving a child" if s == "Child" else "Collision not involving a child")
x["year"] = x.date.dt.year
x["label"] = x.apply(lambda row: "C" + str(row.year) if row.age_group_of_casualty == "Child" else row.year, axis = 1)

y = pd.read_csv("school site.csv")
y["type"] = "School"
y["label"] = y["name"]

y["distance_to_collision"] = pd.np.nan
for index, row in y.iterrows():
    school = (row.latitude, row.longitude)
    d = x.apply(lambda r: geodesic(school, (r.latitude, r.longitude)).meters, axis = 1)
    y.loc[index, "distance_to_collision"] = min(d)

z = pd.read_csv("completed crossing.csv")
z["type"] = "Completed crossing"
z["label"] = z.year.astype(str)

w = pd.read_csv("possible crossing.csv")
w["type"] = "Possible crossing"
w["label"] = w.avg_four_peak_adpv2.apply(lambda x: "%.2f" % x)

v = pd.concat([x, y, z, w])

v.to_csv("combined.csv", index = False)