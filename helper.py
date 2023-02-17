import pandas as pd
from pathlib import Path
import csv
from scipy import spatial
import simplekml


def merge_files(directory):
    merged_df = pd.DataFrame()
    for filepath in Path(directory).glob("*filtered.csv"):
        print(filepath)
        df = pd.read_csv(filepath)
        merged_df = pd.concat([merged_df, df])
    return merged_df


def sort_by_time(df):
    df["datetime"] = pd.to_datetime(df["# Timestamp"])
    df = df.sort_values(by="datetime", ascending=False)
    df = df.drop("datetime", axis=1)
    return df


def save_analysis(pivot_json, filepath):
    p = [{"MMSI": key, "points": len(pivot_json[key])} for key in pivot_json]
    with open(filepath, "w") as f:
        writer = csv.DictWriter(f, ["MMSI", "points"])
        writer.writeheader()
        writer.writerows(p)


def merge_original_data(directory, slice=["Latitude", "Longitude"]):
    merged_df = pd.DataFrame()
    for filepath in Path(directory).glob("*.csv"):
        print(filepath)
        df = pd.read_csv(filepath)
        df = df.loc[:, slice]
        merged_df = pd.concat([merged_df, df])
    # Filter our weird shit outside of europe
    merged_df = merged_df.loc[
        (merged_df["Latitude"] >= 50)
        & (merged_df["Latitude"] <= 66)
        & (merged_df["Longitude"] >= -10)
        & (merged_df["Longitude"] <= 30)
    ]
    return merged_df


def convex_hull(df, filename="convex_hull.kml"):
    sample = df.sample(frac=0.25).to_numpy()
    hull = spatial.ConvexHull(sample, qhull_options="Qt")
    hull_indices = hull.vertices
    points = sample[hull_indices]
    kml = simplekml.Kml()
    for point in points:
        kml.newpoint(name="Hull Point", coords=[(point[1], point[0])])
    kml.save(filename)
