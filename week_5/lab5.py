import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error


# Function: execute and print results of SQL query
def dbexec(conn, query):
    with conn.cursor() as cursor:
        cursor.execute(query)
        for tb in cursor:
            print(tb)


def main():
    try:
        with connect(
            host="fosmysqlprd01.its.auckland.ac.nz",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
            autocommit=True
        ) as connection:

            # 1: Show all databases
            # TODO: Call dbexec with a query to show all databases
            pass

            # 2: Select a database and show its tables
            dbname = input("\nEnter a database: ")
            # TODO: Use the selected database
            # TODO: Show all tables in that database
            pass

            # Let user select a table and view all rows
            table = input("\nEnter a table name to SELECT * from: ")
            # TODO: Select and display all rows in the chosen table
            pass

            # 3: Insert a new instructor record
            print("Inserting a new instructor record into the table...")
            # TODO: Add insert statement

            try:
             # TODO: Call dbexec with a query to insert
                print("Insert successful.")
            except Error as e:
                print("Error:", e)

            # 4: Optional query loop
            while True:
                user_query = input("\n(Optional) Enter a SQL to execute or 'exit' to finish: ")
                if user_query.lower() == "exit":
                    break
                try:
                    # TODO: Execute the user's query
                    pass
                except Error as e:
                    print("Error:", e)

    except Error as e:
        print(e)


main()
