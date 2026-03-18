import pandas as pd

print("\n========== LOADING CSV DATA ==========\n")

# Load CSV file
df = pd.read_csv("files/employees.csv")

print(df)
# Convert JoinDate to datetime
df["JoinDate"] = pd.to_datetime(df["JoinDate"])

print(df)


# ---------------------------------------------------
# BASIC GROUPBY
# ---------------------------------------------------

print("\n========== Average Salary by Department ==========\n")

avg_salary = df.groupby("Department")["Salary"].mean()

print(avg_salary)


# ---------------------------------------------------
# COUNT EMPLOYEES
# ---------------------------------------------------

print("\n========== Number of Employees per Department ==========\n")

count_emp = df.groupby("Department")["EmployeeID"].count()

print(count_emp)


# ---------------------------------------------------
# MULTIPLE AGGREGATIONS
# ---------------------------------------------------

print("\n========== Salary Statistics per Department ==========\n")

salary_stats1 = df.groupby("Department")["Salary"].agg(["mean", "max", "min"])
print(salary_stats1)
salary_stats2=df.groupby("Department")["Salary"].agg(low_score="min",high_score="max")
print(salary_stats2)


# ---------------------------------------------------
# GROUP BY MULTIPLE COLUMNS
# ---------------------------------------------------

print("\n========== Average Salary per Department and Gender ==========\n")

multi_group = df.groupby(["Department","Gender"])["Salary"].mean()

print(multi_group)


# ---------------------------------------------------
# TRANSFORM (Add group average to each row)
# ---------------------------------------------------

print("\n========== Adding Department Average Salary Column ==========\n")

df["Dept_Avg_Salary"] = df.groupby("Department")["Salary"].transform("mean")

print(df)


# ---------------------------------------------------
# FILTER GROUPS
# ---------------------------------------------------

print("\n========== Departments with Avg Salary > 85000 ==========\n")

filtered = df.groupby("Department").filter(lambda x: x["Salary"].mean() > 85000)

print(filtered)


# ---------------------------------------------------
# SORT RESULTS
# ---------------------------------------------------

print("\n========== Highest Paid Departments ==========\n")

sorted_salary = df.groupby("Department")["Salary"].mean().sort_values(ascending=False)

print(sorted_salary)


print("\n========== PRACTICE COMPLETE ==========\n")