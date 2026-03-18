
import pandas as pd

df = pd.read_csv("files/sample_sort_operations.csv")

print(df.sort_values("Age"))
# print(df.sort_values("Age", ascending=False))
print(df.sort_values(["Age", "Salary"]))
df.reset_index(drop=True, inplace=True)
print(df.sort_index())
# 
df["Rank"] = df["Score"].rank()
print(df["Rank"])
# 
df["Rank"] = df["Score"].rank(method="dense")
print(df["Rank"])

df.rename(columns={"Name": "FullName"}, inplace=True)
df.rename(index={0: "row1", 1: "row2"}, inplace=True)

df.columns = ["FullName", "Age", "City", "Salary", "Score", "Rank"]
df = df[["City", "FullName", "Age"]]

cols = ["FullName"] + [col for col in df.columns if col != "FullName"]
df = df[cols]

print(df)
