import pandas as pd
import numpy as np

# Generate 400 sample records
np.random.seed(42)

names = ["John", "Anna", "Mike", "Sara", "Tom", "Rita", "Alex", "Sam"]
cities = ["Delhi", "Mumbai", "Pune", "Bangalore", "Hyderabad"]
genders = ["M", "F"]
categories = ["A", "B", "C"]

data = {
    "Name": np.random.choice(names, 400),
    "Age": np.random.randint(15, 60, 400),
    "Gender": np.random.choice(genders, 400),
    "City": np.random.choice(cities, 400),
    "Email": [f"user{i}@example.com" for i in range(400)],
    "Date": pd.date_range("2024-01-01", periods=400).astype(str),
    "Category": np.random.choice(categories, 400),
}

df = pd.DataFrame(data)

# Save CSV
filepath = "sample_data_400.csv"
df.to_csv(filepath, index=False)

filepath
