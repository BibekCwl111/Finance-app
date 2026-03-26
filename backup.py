import shutil


def backup_database():
    try:
        shutil.copy("finance.db", "backup_finance.db")
        print("Backup created successfully!")

    except FileNotFoundError:
        print("Database file not found!")


def restore_database():
    try:
        shutil.copy("backup_finance.db", "finance.db")
        print("Database restored successfully!")

    except FileNotFoundError:
        print("Backup file not found!")