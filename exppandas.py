# 1. Create a student dictionary, convert it into a DataFrame, calculate total and average marks, and display students scoring above 75% average.

import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Sneha"],
    "Python": [80, 70, 90, 85, 60],
    "DBMS": [75, 80, 85, 90, 65],
    "Maths": [85, 75, 95, 80, 70]
}

df = pd.DataFrame(data)

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print(df)
print("Students scoring above 75 average:")
print(df[df["Average"] > 75])