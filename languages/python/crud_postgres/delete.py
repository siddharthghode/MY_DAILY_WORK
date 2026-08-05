from db import conn, cursor
from read import show_tables, view_records


def delete_record():

    try:

        # Show available tables
        show_tables()

        table_name = input("\nEnter Table Name: ").strip()

        # Show records
        print()
        view_records(table_name)

        # Select record
        record_id = input("\nEnter ID to Delete: ").strip()

        # Get column names
        cursor.execute("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = %s
            ORDER BY ordinal_position;
        """, (table_name,))

        columns = [col[0] for col in cursor.fetchall()]

        # Fetch selected record
        cursor.execute(
            f"SELECT * FROM {table_name} WHERE id = %s",
            (record_id,)
        )

        record = cursor.fetchone()

        if record is None:
            print("\nRecord not found.")
            return

        # Display record
        print("\n========== RECORD ==========\n")

        for col, value in zip(columns, record):
            print(f"{col:<15}: {value}")

        print("\n============================")

        confirm = input(
            "\nAre you sure you want to delete this record? (y/n): "
        ).lower()

        if confirm != "y":
            print("\nDeletion cancelled.")
            return

        cursor.execute(
            f"DELETE FROM {table_name} WHERE id = %s",
            (record_id,)
        )

        conn.commit()

        print("\n✅ Record deleted successfully!")

    except Exception as e:

        conn.rollback()

        print("Error:", e)


def drop_table():

    show_tables()

    table_name = input("\nEnter Table Name: ").strip()

    confirm = input(
        f"Are you sure you want to drop '{table_name}'? (y/n): "
    ).lower()

    if confirm != "y":
        print("\nOperation cancelled.")
        return

    try:

        cursor.execute(f"DROP TABLE {table_name}")

        conn.commit()

        print("\n✅ Table dropped successfully!")

    except Exception as e:

        conn.rollback()

        print("Error:", e)