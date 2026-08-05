from db import conn, cursor
from read import show_tables, view_records


def update_record():

    try:

        # Show tables
        show_tables()

        table_name = input("\nEnter Table Name: ").strip()

        # Show all records
        print()
        view_records(table_name)

        # Select record
        record_id = input("\nEnter ID to Update: ").strip()

        # Get column names
        cursor.execute("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = %s
            ORDER BY ordinal_position;
        """, (table_name,))

        columns = [col[0] for col in cursor.fetchall()]

        # Get selected record
        cursor.execute(
            f"SELECT * FROM {table_name} WHERE id=%s",
            (record_id,)
        )

        record = cursor.fetchone()

        if record is None:
            print("\nRecord not found.")
            return

        # Show current record
        print("\n========== CURRENT RECORD ==========\n")

        for col, value in zip(columns, record):
            print(f"{col:<15}: {value}")

        print("\n=====================================")

        # Editable columns
        editable = []

        print("\nSelect Columns to Update\n")

        count = 1

        for col in columns:

            if col in ("id", "created_at", "updated_at"):
                continue

            editable.append(col)

            print(f"{count}. {col}")

            count += 1

        choices = input(
            "\nEnter column numbers (comma separated): "
        )

        selected = [
            int(x.strip())
            for x in choices.split(",")
        ]

        updates = []
        values = []

        print()

        for choice in selected:

            column = editable[choice - 1]

            new_value = input(f"Enter new {column}: ")

            updates.append(f"{column} = %s")
            values.append(new_value)

        updates.append("updated_at = CURRENT_TIMESTAMP")

        query = f"""
        UPDATE {table_name}
        SET {", ".join(updates)}
        WHERE id = %s;
        """

        values.append(record_id)

        cursor.execute(query, values)

        conn.commit()

        print("\n✅ Record Updated Successfully!")

    except Exception as e:

        conn.rollback()

        print("\nError:", e)