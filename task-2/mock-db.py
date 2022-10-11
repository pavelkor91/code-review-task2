import sqlite3

def create_and_fill_db():
    con = sqlite3.connect('db.sqlite')
    cur = con.cursor()

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS users(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT,
       email TEXT);

    CREATE TABLE IF NOT EXISTS subjects(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT);
    
    CREATE TABLE IF NOT EXISTS results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        result FLOAT,
        subject INTEGER,
        FOREIGN KEY (user_id) REFERENCES user(id)
        FOREIGN KEY (subject) references subjects(id));
    """)

    con.commit()

    subjects = [('История',),('Математика',),('Физика',),('Химия',),('Физкультура',),('Английский',)]
    con.executemany('INSERT INTO subjects(name) VALUES(?)', subjects)
    con.commit()

    users = [
        ('Иван','ivan@tst.ru'),
        ('Владимир','vladimir@tst.ru'),
        ('Кирилл','kirill@tst.ru'),
        ('Александр','alex@tst.ru'),
        ('Степан','stepan@tst.ru'),
        ('Юлия','ulia@tst.ru'),
        ('Ирина','irina@tst.ru'),
    ]

    con.executemany('INSERT INTO users(name,email) VALUES(?, ?)', users)
    con.commit()

    results = [
        (1, 85.5, 1),
        (1, 63.2, 2),
        (1, 62.1, 3),
        (1, 45.8, 4),
        (1, 75.9, 6),

        (2, 85.5, 1),
        (2, 90.5, 3),
        (2, 51.6, 6),
        (2, 47.5, 2),


        (3, 70.5, 2),
        (3, 51.5, 3),
        (3, 21.5, 4),
        (3, 5.5, 5),
        (3, 61.5, 6),


        (4, 15.5, 1),
        (4, 100.0, 2),
        (4, 100.0, 3),



        (5, 67.5, 1),
        (5, 44.5, 3),
        (5, 51.5, 4),
        (5, 66.5, 6),

        (6, 76.5, 1),
        (6, 88.5, 2),
        (6, 61.5, 3),
        (6, 99.5, 4),
        (6, 99.7, 5)
    ]

    con.executemany('INSERT INTO results(user_id,result,subject) VALUES(?, ?, ?)', results)
    con.commit()

    con.close()

if __name__ == '__main__':
    create_and_fill_db()

