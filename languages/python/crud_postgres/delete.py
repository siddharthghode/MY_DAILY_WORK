from db import conn, cursor

query = """
DELETE FROM employee WHERE id = %s
"""

cursor.execute(query,(1,))

conn.commit()

print("Employee deleted successfully!")

cursor.close()
conn.close()