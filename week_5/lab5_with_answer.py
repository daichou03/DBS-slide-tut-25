import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

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
            # 2.1
            dbexec(connection, "SHOW DATABASES")

            # 2.2
            dbname = input("\nEnter a database: ")
            dbexec(connection, f"USE {dbname}")
            dbexec(connection, "SHOW TABLES")


            table = input("\nEnter a table name to SELECT * from: ")
            dbexec(connection, f"SELECT * FROM {table}")

            # 2.3
            print("Inserting a new instructor record into the table...")
            insert = """
            INSERT INTO instructor (ID, name, dept_name, salary)
            VALUES (19990, 'TestUser', 'Finance', 70000.00)
            """
            try:
                dbexec(connection, insert)
                print("Insert successful.")
            except Error as e:
                print("Error:", e)

            # 2.4
            while True:
                user_query = input("\n(Optional) Enter a SQL to execute or 'exit' to finish: ")
                if user_query.lower() == "exit":
                    break
                try:
                    dbexec(connection, user_query)
                except Error as e:
                    print("Error:", e)

    except Error as e:
        print(e)

main()
