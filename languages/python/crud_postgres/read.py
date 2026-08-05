from db import cursor


def show_tables():

    try:

        cursor.execute("""
            SELECT tablename
            FROM pg_tables
            WHERE schemaname = 'public'
            ORDER BY tablename;
        """)

        tables = cursor.fetchall()

        if not tables:
            print("\nNo tables found.")
            return

        print("\n========== AVAILABLE TABLES ==========")

        for table in tables:
            print(table[0])

        print("======================================")

    except Exception as e:
        print("Error:", e)


def describe_table():

    show_tables()

    table_name = input("\nEnter Table Name: ")

    try:

        cursor.execute("""
            SELECT
                column_name,
                data_type,
                is_nullable
            FROM information_schema.columns
            WHERE table_name = %s
            ORDER BY ordinal_position;
        """, (table_name,))

        columns = cursor.fetchall()

        if not columns:
            print("Table not found.")
            return

        print(f"\n========== {table_name.upper()} ==========")
        print(f"{'COLUMN':20} {'TYPE':20} {'NULLABLE'}")
        print("-" * 50)

        for column in columns:
            print(f"{column[0]:20} {column[1]:20} {column[2]}")

    except Exception as e:
        print("Error:", e)


def view_records(table_name=None):

    if table_name is None:
        show_tables()
        table_name = input("\nEnter Table Name: ")

    try:

        cursor.execute(f"SELECT * FROM {table_name}")

        rows = cursor.fetchall()

        if not rows:
            print("\nNo Records Found.")
            return

        print("\n========== RECORDS ==========\n")

        for row in rows:
            print(row)

    except Exception as e:
        print("Error:", e)