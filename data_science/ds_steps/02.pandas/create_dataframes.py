import pandas as pd

df = pd.read_csv("contacts.csv")
print(df)
print("\n")

ef = pd.read_excel("contacts.xlsx")
print(ef)

bg = pd.read_csv("downdata.csv")
print(bg)
print("\n")

print(type(df))
print(bg.describe())

# Correct way to print column names:
print(bg.columns)
# or
print(list(df.columns))
sort=bg.sort_values('IMDb')
print(sort)