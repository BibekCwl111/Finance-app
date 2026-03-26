from auth import register_user, login_user
from transactions import (
    add_transaction,
    view_transactions,
    delete_transaction
)
from reports import (
    monthly_report,
    yearly_report
)

from budget import set_budget 
from backup import backup_database,restore_database


def user_menu(user_id):
    while True:
        print("\n===== User Menu =====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Delete Transaction")
        print("4. Monthly Report")
        print("5. Yearly Report")
        print("6. Set Budget")
        print("7. Backup Data")
        print("8. Restore Data")
        print("9. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            add_transaction(user_id)

        elif choice == "2":
            view_transactions(user_id)

        elif choice == "3":
            delete_transaction(user_id)

        elif choice == "4":
            monthly_report(user_id)

        elif choice == "5":
            yearly_report(user_id)

        elif choice == "6":
            set_budget(user_id)

        elif choice == "7":
            backup_database()

        elif choice == "8":
            restore_database()

        elif choice == "9":
            print("Logged out.")
            break

        else:
            print("Invalid choice!")


def main():
    while True:
        print("\n===== Personal Finance App =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register_user()

        elif choice == "2":
            user_id = login_user()

            if user_id:
                user_menu(user_id)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()