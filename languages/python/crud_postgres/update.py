from db import conn, cursor

query = """
UPDATE employee
SET name = %s, age = %s
WHERE id = %s
"""

cursor.execute(query, ("Siddharth", 23, 1))

conn.commit()

print("Employee updated successfully!")

cursor.close()
conn.close()