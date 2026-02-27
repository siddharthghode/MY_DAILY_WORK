import pandas as pd

# ------------------ SAMPLE DATAFRAME FOR DATA CLEANING ------------------
df=pd.read_csv("sample_data_400.csv")


print("Original DataFrame:\n", df, "\n")

# ------------------ MISSING VALUE CHECKS ------------------
print("df.isnull():\n", df.isnull(), "\n")
print("df.isnull().sum():\n", df.isnull().sum(), "\n")

print("Rows after dropna():\n", df.dropna(), "\n")
print("Columns after dropna(axis=1):\n", df.dropna(axis=1), "\n")

print("Fill NaN with 0:\n", df.fillna(0), "\n")
print("Age filled with mean:\n", df["Age"].fillna(df["Age"].mean()), "\n")
print("Forward fill:\n", df.ffill(), "\n")
print("Backward fill:\n", df.bfill(), "\n")

# ------------------ DUPLICATES ------------------
print("df.duplicated():\n", df.duplicated(), "\n")
print("Drop duplicates:\n", df.drop_duplicates(), "\n")
print("Duplicates on Name & Age:\n", df.duplicated(subset=["Name", "Age"]), "\n")

# ------------------ STRING OPERATIONS ------------------
print("Name lowercase:\n", df["Name"].str.lower(), "\n")
print("City contains delhi:\n", df["City"].str.contains("delhi", case=False, na=False), "\n")
print("Email split @:\n", df["Email"].str.split("@"), "\n")

# ------------------ TYPE CONVERSIONS ------------------
df["Age"] = df["Age"].astype("float32")  # example
print("Converted Age dtype:\n", df.dtypes, "\n")

# Date conversion using to_datetime() (special handling)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Category type
df["Category"] = df["Category"].astype("category")
print("After type conversion:\n", df.dtypes, "\n")

# ------------------ APPLY, MAP, REPLACE ------------------
df["Age Group"] = df["Age"].apply(lambda x: "Adult" if x >= 18 else "Minor")

# map gender
gender_map = {"M": "Male", "F": "Female"}
df["Gender"] = df["Gender"].map(gender_map)

# replace city abbreviations
df["City"] = df["City"].replace({"Del": "Delhi", "Mum": "Mumbai"})

print("Final cleaned DataFrame:\n", df)
