import pandas as pd
employees = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "DeptID": [10, 20, 30]
})

departments = pd.DataFrame({
    "DeptID": [10, 20, 40],
    "DeptName": ["HR", "Engineering", "Marketing"]
})



print("\n========== INNER MERGE ==========")
print("Only matching rows from both employees and departments\n")

merge = pd.merge(employees, departments, on="DeptID")
print(merge)


print("\n========== LEFT MERGE ==========")
print("All rows from employees + matching rows from departments\n")

left = pd.merge(employees, departments, on="DeptID", how="left")
print(left)


print("\n========== RIGHT MERGE ==========")
print("All rows from departments + matching rows from employees\n")

right = pd.merge(employees, departments, on="DeptID", how="right")
print(right)


print("\n========== OUTER MERGE ==========")
print("All rows from both tables (full join)\n")

outer = pd.merge(employees, departments, on="DeptID", how="outer")
print(outer)

print("----------------CONCATENATING------------")
df1 = pd.DataFrame({"Name": ["Alice", "Bob"]})
df2 = pd.DataFrame({"Name1": ["Charlie", "David"]})
ct1=pd.concat([df1, df2])
print(ct1)
print("\n\n")

df1 = pd.DataFrame({"ID": [1, 2]})
df2 = pd.DataFrame({"Score": [90, 80]})
ct2=pd.concat([df1, df2])
print(ct2)