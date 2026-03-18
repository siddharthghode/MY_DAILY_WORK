"""
Pandas File Handling Practice
Author: Sid
Goal: Learn how to read and write CSV, Excel, and JSON files using Pandas
"""

import pandas as pd


# ---------------------------------------------------
# 1. READ CSV FILE
# ---------------------------------------------------

print("\n--- Reading CSV File ---")

# Basic read
df = pd.read_csv("files/data1.csv")

print(df)


# ---------------------------------------------------
# 2. READ SPECIFIC COLUMNS
# ---------------------------------------------------

print("\n--- Reading Specific Columns ---")

df_cols = pd.read_csv("files/data1.csv", usecols=["Name", "Age"])

print(df_cols)


# ---------------------------------------------------
# 3. READ LIMITED ROWS
# ---------------------------------------------------

print("\n--- Reading Limited Rows ---")

df_rows = pd.read_csv("files/data1.csv", nrows=5)

print(df_rows)


# ---------------------------------------------------
# 4. FILTER DATA
# ---------------------------------------------------

print("\n--- Filtering Data (IMDb > 6) ---")

df_filtered = df[df["IMDb"] > 6]

print(df_filtered)


# ---------------------------------------------------
# 5. SAVE DATA TO CSV
# ---------------------------------------------------

print("\n--- Writing CSV File ---")

df_filtered.to_csv("files/data_updated.csv", index=False)

print("File saved as data_updated.csv")


# ---------------------------------------------------
# 6. READ EXCEL FILE
# ---------------------------------------------------

print("\n--- Reading Excel File ---")

df_excel = pd.read_excel("files/data1.xlsx")

print(df_excel)


# ---------------------------------------------------
# 7. READ SPECIFIC SHEET
# ---------------------------------------------------

print("\n--- Reading Specific Sheet ---")

df_sheet = pd.read_excel("files/data1.xlsx", sheet_name="Sales")

print(df_sheet)


# ---------------------------------------------------
# 8. WRITE EXCEL FILE
# ---------------------------------------------------

print("\n--- Writing Excel File ---")

df_excel.to_excel("files/output.xlsx", index=False)

print("Excel file saved as output.xlsx")


# ---------------------------------------------------
# 9. READ JSON FILE
# ---------------------------------------------------

print("\n--- Reading JSON File ---")

df_json = pd.read_json("files/my.json")

print(df_json)


# ---------------------------------------------------
# 10. DATAFRAME INFORMATION
# ---------------------------------------------------

print("\n--- Data Information ---")

print(df.info())


# ---------------------------------------------------
# 11. BASIC DATA ANALYSIS
# ---------------------------------------------------

print("\n--- Basic Statistics ---")

print(df.describe())


# ---------------------------------------------------
# 12. HEAD AND TAIL
# ---------------------------------------------------

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Last 5 Rows ---")
print(df.tail())