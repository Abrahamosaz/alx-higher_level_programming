#!/usr/bin/python3
"""script to connect to the database and select data from the server"""


def filter_states(username, password, db):
    """function to connect to the database base on command line argument"""
    db_engine = MySQLdb.connect(
            host='localhost',
            user=username,
            password=password,
            database=db
            )
    conn = db_engine.cursor()
    conn.execute("SELECT * FROM states WHERE name LIKE 'N%' \
                 ORDER BY states.id")
    return conn.fetchall()


if __name__ == "__main__":
    import MySQLdb
    import sys
    result = filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
    for data in result:
        print(data)
