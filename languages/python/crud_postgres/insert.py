from db import conn, cursor
from read import show_tables


def insert_record():

    try:
        # Show available tables
        show_tables()

        table_name = input("\nEnter Table Name: ").strip()

        # Check if table exists and get its columns
        cursor.execute("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = %s
            ORDER BY ordinal_position;
        """, (table_name,))

        columns = cursor.fetchall()

        if not columns:
            print("\nTable does not exist.")
            return

        column_names = []
        values = []

        print("\n========== ENTER RECORD ==========\n")

        for column in columns:

            column = column[0]

            # Skip auto-generated columns
            if column in ("id", "created_at", "updated_at"):
                continue

            value = input(f"Enter {column}: ").strip()

            column_names.append(column)
            values.append(value)

        # Create placeholders
        placeholders = ", ".join(["%s"] * len(values))

        # Create column list
        columns_sql = ", ".join(column_names)

        # Final query
        query = f"""
        INSERT INTO {table_name}
        ({columns_sql})
        VALUES ({placeholders});
        """

        cursor.execute(query, values)
        conn.commit()

        print("\n✅ Record inserted successfully!")

    except Exception as e:
        conn.rollback()
        print("\nError while inserting record.")
        print(e)