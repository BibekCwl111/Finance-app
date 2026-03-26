import sqlite3


def monthly_report(user_id):
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    # Total income
    cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE user_id=?
        AND type='income'
        AND strftime('%m', date)=?
        AND strftime('%Y', date)=?
    """, (user_id, month, year))

    income = cursor.fetchone()[0] or 0

    # Total expense
    cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE user_id=?
        AND type='expense'
        AND strftime('%m', date)=?
        AND strftime('%Y', date)=?
    """, (user_id, month, year))

    expense = cursor.fetchone()[0] or 0

    savings = income - expense

    conn.close()

    print("\n===== Monthly Report =====")
    print("Month:", month, "/", year)
    print("Total Income:", income)
    print("Total Expense:", expense)
    print("Savings:", savings)


def yearly_report(user_id):
    year = input("Enter year (YYYY): ")

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    # Total income
    cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE user_id=?
        AND type='income'
        AND strftime('%Y', date)=?
    """, (user_id, year))

    income = cursor.fetchone()[0] or 0

    # Total expense
    cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE user_id=?
        AND type='expense'
        AND strftime('%Y', date)=?
    """, (user_id, year))

    expense = cursor.fetchone()[0] or 0

    savings = income - expense

    conn.close()

    print("\n===== Yearly Report =====")
    print("Year:", year)
    print("Total Income:", income)
    print("Total Expense:", expense)
    print("Savings:", savings)