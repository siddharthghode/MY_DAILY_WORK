from db import conn, cursor

query = """
UPDATE employee
SET name = %s, age = %s, email = %s, date_of_birth = %s, updated_at = CURRENT_TIMESTAMP
WHERE id = %s
"""

cursor.execute(query, ("Siddharth", 25, "siddharth@gmail.com", '2003-07-19', 6))

conn.commit()

print("Employee updated successfully!")

cursor.close()
conn.close()
