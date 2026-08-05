from create import create_table
from read import show_tables,describe_table,view_records
from update import update_record
from delete import delete_record, drop_table
from insert import insert_record


while True:

    print("\n========== DATABASE MENU ==========")
    print("1. Create Table")
    print("2. Show Tables")
    print("3. Describe Table")
    print("4. Insert Record")
    print("5. View Records")
    print("6. Update Record")
    print("7. Delete Record")
    print("8. Drop Table")
    print("9. Exit")
    print("===================================")

    choice = input("Enter Choice : ")
    
    match choice:
        case "1":
            create_table()
        case "2":
            show_tables()
        case "3":
            describe_table()
        case "4":
            insert_record()
        case "5":
            view_records()
        case "6":
            update_record()
        case "7":
            delete_record()
        case "8":
           drop_table()
        case "9":
            print("Good Bye!")
            break
        case _:
            print("Invalid Choice")