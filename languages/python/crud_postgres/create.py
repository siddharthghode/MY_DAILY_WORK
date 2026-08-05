# create.py

from db import conn, cursor


def create_table():
    print("\n========== CREATE TABLE ==========\n")

    table_name = input("Enter Table Name: ").strip()

    if table_name == "":
        print("❌ Table name cannot be empty.")
        return

    try:
        total_columns = int(input("Enter Number of Columns: "))

        if total_columns <= 0:
            print("❌ Table must contain at least one column.")
            return

    except ValueError:
        print("❌ Please enter a valid number.")
        return

    columns = []

    for i in range(total_columns):

        print(f"\n---------- Column {i + 1} ----------")

        column_name = input("Column Name: ").strip()

        if column_name == "":
            print("❌ Column name cannot be empty.")
            return

        print("""
Choose Data Type

1. INT
2. VARCHAR
3. TEXT
4. DATE
5. BOOLEAN
6. DECIMAL
7. FLOAT
8. TIMESTAMP
""")

        datatype_choice = input("Enter Choice: ").strip()

        if datatype_choice == "1":
            datatype = "INT"

        elif datatype_choice == "2":
            length = input("VARCHAR Length: ").strip()
            datatype = f"VARCHAR({length})"

        elif datatype_choice == "3":
            datatype = "TEXT"

        elif datatype_choice == "4":
            datatype = "DATE"

        elif datatype_choice == "5":
            datatype = "BOOLEAN"

        elif datatype_choice == "6":
            precision = input("Precision (Example: 10): ").strip()
            scale = input("Scale (Example: 2): ").strip()
            datatype = f"DECIMAL({precision},{scale})"

        elif datatype_choice == "7":
            datatype = "FLOAT"

        elif datatype_choice == "8":
            datatype = "TIMESTAMP"

        else:
            print("❌ Invalid datatype selected.")
            return

        # NOT NULL
        not_null = input("NOT NULL? (y/n): ").lower()

        # UNIQUE
        unique = input("UNIQUE? (y/n): ").lower()

        constraint = ""

        if not_null == "y":
            constraint += " NOT NULL"

        if unique == "y":
            constraint += " UNIQUE"

        columns.append(f"{column_name} {datatype}{constraint}")

    query = f"""
    CREATE TABLE {table_name} (
        id SERIAL PRIMARY KEY,
        {', '.join(columns)},
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    try:
        cursor.execute(query)
        conn.commit()

        print("\n✅ Table created successfully!")

    except Exception as e:
        conn.rollback()
        print("\n❌ Error while creating table.")
        print(e)