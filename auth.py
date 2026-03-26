import sqlite3

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        print("Registration successful!")

    except sqlite3.IntegrityError:
        print("Username already exists!")

    conn.close()


def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        print("Login successful!")
        return user[0]   # user_id return করবে
    else:
        print("Invalid username or password!")
        return None