import mysql.connector
from contextlib import  contextmanager

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "expense_manager"

    )
    if connection.is_connected():
        print("Connection Successful")
    else:
        print("Connection Failed")

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()

    cursor.close()
    connection.close()

def fetch_records():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expense_manager.expenses")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def fetch_records_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses where expense_date=%s", (expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

def insert_expense(expense_date,amount,category,notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "Insert into expenses(expense_date,amount,category,notes) values (%s,%s,%s,%s)",(expense_date,amount,category,notes))

def delete_expense(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "Delete from expenses where expense_date = %s",(expense_date,))

if __name__ == "__main__":
    #fetch_records()
    #insert_expense("2024-08-20",300,"Food","Panipuri")
    fetch_records_date("2024-08-20")
    #delete_expense("2024-08-20")
    #fetch_records_date("2024-08-20")
