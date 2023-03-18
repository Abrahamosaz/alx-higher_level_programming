#!/usr/bin/python3
"""script to connect and print out all the data from the databases"""


def list_states(username, password, db):
    """function for connecting to database"""
    db_engine = MySQLdb.connect(
            host='localhost',
            user=username,
            password=password,
            database=db
            )
    connect = db_engine.cursor()
    connect.execute("SELECT * FROM states ORDER BY states.id ASC")
    return connect.fetchall()


if __name__ == "__main__":
    import sys
    import MySQLdb
    result = list_states(sys.argv[1], sys.argv[2], sys.argv[3])
    for item in result:
        print(item)
