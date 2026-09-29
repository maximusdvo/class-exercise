"""DATA CLEANING AND STUFF"""

from pathlib import Path
import pandas as pd

data_path = Path("data") / "messy_netflix_titles.csv"
df = pd.read_csv(data_path)

is_movie = df["type"] == "Movie"

print(is_movie.head())

movies = df[df["type"] == "Movie"]
print(movies.head())
print(movies.shape)

recent = df[df["release_year"] >= 2020]

#we can use & AND and | for OR and we put them inside the parentheses

recent_movies = df[(df["type"] == "Movie") & (df["release_year"] >= 2020)]

result = df.loc[df["release_year"] >= 2020,["title", "type"]]

print(result.head())

#for duplicating rows

print(df[df.duplicated()])

before = len(df)

df = df.drop_duplicates()

print(f"Removes {before - len(df)} duplicate row(s)")


# for missing values

print(df.isna().sum())

#command above detects the missing values

#command below drops rows containing one or more missing values
rows_dropped = df.dropna()

#command belo drops columns contianign one or more missing values
columns_dropped = df.dropna(axis=1)