import csv
import sqlite3
from constants import authors_db, logs_db, general_csv, comments_csv


def save_csv(header, rows, path):
    with open(path, "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def general_info(user_id):
    con = sqlite3.connect(logs_db)
    cur = con.cursor()
    query = """
    SELECT 
        date(datetime) as date,
        SUM(CASE WHEN event_type_id = 1 THEN 1 ELSE 0 END) AS logins,
        SUM(CASE WHEN event_type_id = 5 THEN 1 ELSE 0 END) AS logouts,
        SUM(CASE WHEN space_type_id = 2 THEN 1 ELSE 0 END) AS blog_events
    FROM logs
        WHERE user_id = ?
        GROUP BY date"""
    cur.execute(query, (user_id,))

    columns = [description[0] for description in cur.description]
    values = cur.fetchall()
    con.close()

    save_csv(columns, values, general_csv)
    print("general.csv - сохранено")


def comments_info(user_id, user_login):
    logs_con = sqlite3.connect(logs_db)
    logs_cur = logs_con.cursor()
    # данные о комментируемых пользователем постах и количестве комментариев
    query = """
    SELECT 
        post_id,
        COUNT(post_id) as comment_count
    FROM logs
        WHERE user_id = ? AND event_type_id=2
        GROUP BY post_id
    """
    logs_cur.execute(query, (user_id,))
    logs_res = logs_cur.fetchall()
    post_ids = ",".join([str(row[0]) for row in logs_res])
    logs_columns = [description[0] for description in logs_cur.description]

    authors_con = sqlite3.connect(authors_db)
    authors_cur = authors_con.cursor()
    # данные о логине автора поста и заголовке
    query = f"""
    SELECT 
        users.login as author_login,
        header
    FROM post
    JOIN users ON users.id=post.author_id
        WHERE post.id IN ({post_ids})
    """
    authors_cur.execute(query)
    authors_columns = [description[0] for description in authors_cur.description]
    authors_res = authors_cur.fetchall()

    columns = ("user_login", authors_columns[1], authors_columns[0], logs_columns[1])
    values = []
    for i in range(len(logs_res)):
        values.append(
            (user_login, authors_res[i][1], authors_res[i][0], logs_res[i][1])
        )

    save_csv(columns, values, comments_csv)
    print("comments.csv - сохранено")


def get_user_id(login):
    con = sqlite3.connect(authors_db)
    cur = con.cursor()
    query = """
    SELECT id 
    FROM users 
    WHERE login = ?
    """
    cur.execute(query, (login,))

    res = cur.fetchone()
    if res == None:
        return -1
    return res[0]


def main():
    login = input("Введите логин пользователя: ")
    user_id = get_user_id(login)
    if user_id == -1:
        print(f"Пользователь с логином {login} не найден")
        exit()

    print(f"Пользователь {login} найден")
    general_info(user_id)
    comments_info(user_id, login)


if __name__ == "__main__":
    main()
