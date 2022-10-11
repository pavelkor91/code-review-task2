import sqlite3

def get_results():

    con = sqlite3.connect('db.sqlite')
    cur = con.cursor()

    cur.execute('''
        SELECT users.name, results.result, subjects.name
        FROM results
        JOIN users ON users.id==results.user_id
        JOIN subjects ON subjects.id==results.subject
        ORDER BY results.result DESC
        LIMIT 3;
    ''')

    for result in cur:
        print(result)

    print('Task *:')
    cur.execute('''
        SELECT users.name, sum(results.result) AS exam_sum
        FROM results
        JOIN users ON users.id==results.user_id
        GROUP BY users.id
        HAVING exam_sum > 200 AND count(results.result)=3
        ORDER BY exam_sum DESC
        LIMIT 3;
    ''')

    for result in cur:
        print(result)

    con.close()

if __name__ == '__main__':
    get_results()
