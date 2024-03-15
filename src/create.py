import sqlite3
from constants import authors_db, logs_db

sqlscript_init_authors = "sql/init_authors.sql"
sqlscript_fill_authors = "sql/fill_authors.sql"

sqlscript_init_logs = "sql/init_logs.sql"
sqlscript_fill_logs = "sql/fill_logs.sql"


def execute_sql(database_path, script_path):
    con = sqlite3.connect(database_path)
    cur = con.cursor()

    with open(script_path) as script:
        cur.executescript(script.read())

    con.commit()
    con.close()


def create_authors_database():
    try:
        execute_sql(authors_db, sqlscript_init_authors)
        execute_sql(authors_db, sqlscript_fill_authors)
        print("authors - база создана и заполнена тестовыми данными")
    except Exception as e:
        print("authors - ошибка:", e)


def create_logs_database():
    try:
        execute_sql(logs_db, sqlscript_init_logs)
        execute_sql(logs_db, sqlscript_fill_logs)
        print("logs - база создана и заполнена тестовыми данными")
    except Exception as e:
        print("logs - ошибка:", e)


def main():
    create_authors_database()
    create_logs_database()


if __name__ == "__main__":
    main()
