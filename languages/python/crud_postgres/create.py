from db import conn, cursor

name = input("Enter employee name: ")
age = int(input("Enter employee age: "))
email = input("Enter employee email: ")
date_of_birth=input("Enter date of birth: ")

query = """
INSERT INTO employee (name, age, email,date_of_birth)
VALUES (%s, %s, %s,%s)
"""

cursor.execute(query, (name, age, email,date_of_birth))

conn.commit()

print("✅ Employee added successfully!")

cursor.close()
conn.close()