import sqlite3
from datetime import datetime
from unicodedata import category
from budget import check_budget

def add_transaction(user_id):
    print("\n1. Add Income")
    print("2. Add Expense")

    choice = input("Choose option: ")

    if choice == "1":
        t_type = "income"
    elif choice == "2":
        t_type = "expense"
    else:
        print("Invalid choice!")
        return

    category = input("Enter category (Food/Rent/Salary/etc): ")
    amount = float(input("Enter amount: "))

    date = datetime.now().strftime("%Y-%m-%d")

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions
        (user_id, type, category, amount, date)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, t_type, category, amount, date))

    conn.commit()
    conn.close()

    if t_type == "expense":
        check_budget(user_id, category)

    print("Transaction added successfully!")


def view_transactions(user_id):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, type, category, amount, date
        FROM transactions
        WHERE user_id=?
    """, (user_id,))

    rows = cursor.fetchall()

    conn.close()

    print("\n===== Your Transactions =====")

    if not rows:
        print("No transactions found.")
        return

    for row in rows:
        print(
            "ID:", row[0],
            "| Type:", row[1],
            "| Category:", row[2],
            "| Amount:", row[3],
            "| Date:", row[4]
        )


def delete_transaction(user_id):
    view_transactions(user_id)

    t_id = input("\nEnter Transaction ID to delete: ")

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM transactions
        WHERE id=? AND user_id=?
    """, (t_id, user_id))

    conn.commit()
    conn.close()

    print("Transaction deleted successfully!")