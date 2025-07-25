import pandas as pd
import os

os.chdir(r"C:\Users\dimit\Documents\My Projects\bexley-road-safety\detailed data")
         

x = pd.read_csv("bexley collision with pedestrian casualty.csv", low_memory = False)

cc = ["accident_index",
      "longitude",
      "latitude",
      "number_of_vehicles",
      "number_of_casualties",
      "date",
      "time",
      "road_type",
      "speed_limit",
      "junction_detail",    
      "pedestrian_crossing_physical_facilities",
      "light_conditions",
      "weather_conditions",
      "road_surface_conditions",
      "sex_of_casualty",
      "age_of_casualty",
      "casualty_severity",
      "pedestrian_location"]

#   "pedestrian_crossing_human_control",
#    "pedestrian_movement"

x = x[cc]

x["road_type"] = x.road_type.map({1: "Roundabout",
             2: "One-way street",
             3: "Dual carriageway",
             6: "Single carriageway",
             7: "Slip road",
             9: "Unknown"})

x["junction_detail"] = x.junction_detail.map({0: "Not at or within 20 metres of junction",
             1: "Roundabout",
             2: "Mini roundabout",
             3: "T or staggered junction",
             5: "Slip road",
             6: "Crossroads",
             7: "Junction more than four arms",
             8: "Using private drive or entrance",
             9: "Other",
             99: "Unknown"})

x["age_group_of_casualty"] = x.age_of_casualty.apply(lambda x: "Adult" if x >= 18 else "Child")

x["sex_of_casualty"] = x.sex_of_casualty.map({1: "Male", 2: "Female"})

x["casualty_severity"] = x.casualty_severity.map({1: "Fatal", 2: "Serious", 3: "Slight"})

x["light_conditions"] = x.light_conditions.map({1: "Daylight", 
                                                4: "Darkness: street lights present and lit",
                                                5: "Darkness: street lights present but unlit",
                                                6: "Darkness: no street lighting",
                                                7: "Darkness: street lighting unknown"})

x["road_surface_conditions"] = x.road_surface_conditions.map({1: "Dry", 
                                                2: "Wet",
                                                3: "Snow",
                                                4: "Frost/Ice",
                                                9: "Unknown"})

x["pedestrian_crossing_physical_facilities"] = x.pedestrian_crossing_physical_facilities.map({0: "No physical crossing facility within 50m", 
                                                1: "Zebra Crossing",
                                                4: "Pelican, puffin, toucan",
                                                5: "Pedestrian phase",
                                                7: "Footbridge or subway",
                                                8: "Central refuge",
                                                9: "Unknown"})

x["pedestrian_location"] = x.pedestrian_location.map({1: "In carriageway, crossing on pedestrian crossing facility",
             2: "In carriageway, crossing within zig-zag lines at crossing approach",
             3: "In carriageway, crossing within zig-zag lines at crossing exit",
             4: "In carriageway, crossing elsewhere within 50m of pedestrian crossing",
             5: "In carriageway, crossing elsewhere",
             6: "On footway or verge",
             7: "On refuge or central island",
             8: "In centre of carriageway, not on refuge",
             9: "In carirageway, not crossing",
             10: "Unknown"})

x.to_csv("bexley collision with pedestrian casualty reduced.csv", index = False) 
