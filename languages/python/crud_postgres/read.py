from db import conn,cursor
query = """ SELECT * FROM employee """

cursor.execute(query)

employees = cursor.fetchall()

for employe in employees:
    print(employe)
    
    
cursor.close()
conn.close()

