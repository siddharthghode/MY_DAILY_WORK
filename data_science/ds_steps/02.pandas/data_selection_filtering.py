import pandas as pd

# ------------------ LOADING CSV ------------------
df = pd.read_csv("books_6k.csv")

# ------------------ BASIC INFO -------------------
print(df)              # prints full DataFrame
print(df.describe())   # numerical summary
print(df.tail())       # last 5 rows
print(df.info())       # column info

print("------------------------------------ FILTERING ------------------------------------")

# This line was WRONG earlier — comparing string column to number
# Remove it or fix it if needed
# print(df["isbn13"] < 30)   # ❌ isbn13 is string → invalid numeric comparison

# Show only selected columns
print(df[["title", "subtitle"]])

# Select row 233 and "title"
print(df.loc[233, ["title"]])

# iloc: first 5 rows, column index 4
print("\n", df.iloc[:5, 4])

# Select row 5 with columns title + authors
print(df.loc[5, ["title", "authors"]])

print("--------------------------------------- FILTERING and COUNTING -------------------------------------")

# Filter rows where rating > 3
print(df[df["average_rating"] > 3])

# Authors contains string + pages < 400
print(df[(df["authors"].str.contains("Agatha Christie")) & (df["num_pages"] < 400)])

print("-------------------------------------------- QUERYING ----------------------------------------------")

# Correct query syntax
print(df.query("num_pages > 25 and average_rating < 1.5"))

print("Use backtick `column name` when column has space.")

print("--------------------------------- REFERENCE VARIABLE in QUERY --------------------------------------")

pages = 100
# Use @ to reference Python variable inside query
print(df.query("num_pages > @pages"))

# ------------------ QUERY RULES ------------------
# 1. Column names without quotes:
#       df.query("num_pages > 50")
# 2. Strings MUST be quoted:
#       df.query("authors == 'Agatha Christie'")
# 3. Multi-condition:
#       df.query("average_rating > 3 and num_pages < 300")
# 4. IN operator:
#       df.query("categories in ['Fiction', 'History']")
# 5. Column names with spaces → wrap in backticks:
#       df.query("`published year` > 2000")