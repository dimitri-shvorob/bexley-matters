from pathlib import Path
import polars as pl

PROJECT_PATH = Path(r"C:\Users\dimit\Documents\GitHub\bexley\lip funding")

db = pl.read_csv(PROJECT_PATH / "borough.csv")        

dg = pl.read_csv(PROJECT_PATH / "data raw.csv")\
     .melt(id_vars = "borough").rename({"variable": "year"})\
     .join(db, how = "outer", on = "borough")\
     .with_columns(value_per_capita = pl.col("value")/pl.col("population"))     

dg.write_csv(PROJECT_PATH / "lip by borough.csv")  
