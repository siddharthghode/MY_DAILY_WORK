import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="company",
    user="sid",
    password="mypassword",
    port=5432
)
cursor = conn.cursor()
print("Connected successfully!")