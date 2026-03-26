import sqlite3


def set_budget(user_id):
    category = input("Enter category (Food/Rent/etc): ")
    amount = float(input("Enter monthly budget amount: "))
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    # Check if budget already exists
    cursor.execute("""
        SELECT id FROM budgets
        WHERE user_id=? AND category=? AND month=? AND year=?
    """, (user_id, category, month, year))

    existing = cursor.fetchone()

    if existing:
        # Update budget
        cursor.execute("""
            UPDATE budgets
            SET amount=?
            WHERE user_id=? AND category=? AND month=? AND year=?
        """, (amount, user_id, category, month, year))

        print("Budget updated successfully!")

    else:
        # Insert new budget
        cursor.execute("""
            INSERT INTO budgets
            (user_id, category, amount, month, year)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, category, amount, month, year))

        print("Budget set successfully!")

    conn.commit()
    conn.close()


def check_budget(user_id, category):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    # Get current month and year from transactions
    cursor.execute("""
        SELECT strftime('%m', 'now'), strftime('%Y', 'now')
    """)
    month, year = cursor.fetchone()

    # Get budget
    cursor.execute("""
        SELECT amount FROM budgets
        WHERE user_id=? AND category=? AND month=? AND year=?
    """, (user_id, category, month, year))

    budget = cursor.fetchone()

    if budget:
        budget_amount = budget[0]

        # Calculate total expense
        cursor.execute("""
            SELECT SUM(amount)
            FROM transactions
            WHERE user_id=?
            AND type='expense'
            AND category=?
            AND strftime('%m', date)=?
            AND strftime('%Y', date)=?
        """, (user_id, category, month, year))

        total_expense = cursor.fetchone()[0] or 0

        if total_expense > budget_amount:
            print("\n⚠️ Warning: Budget exceeded for", category)

    conn.close()