from db import conn,cursor
query = """
INSERT INTO employee (name, age)
VALUES (%s, %s)
"""

cursor.execute(query, ("rohan", 21))
cursor.execute(query, ("ram", 24))

conn.commit()

print("Employee added successfully!")

cursor.close()
conn.close()