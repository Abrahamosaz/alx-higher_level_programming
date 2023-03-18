#!/usr/bin/python3
"""retrieve data from the database server base on command line argument"""


def filter_cities(username, password, db, state_name):
    """return all cities from the database server base on the
    state_name passed to the function"""
    db_engine = MySQLdb.connect(
            host='localhost',
            user=username,
            password=password,
            database=db
            )
    conn = db_engine.cursor()
    conn.execute("SELECT cities.name FROM cities INNER JOIN \
                 states ON cities.state_id = states.id WHERE \
                 states.name=%s ORDER BY cities.id", (state_name,))
    return conn.fetchall()


if __name__ == "__main__":
    import MySQLdb
    import sys
    result = filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    result_list = []
    [result_list.append(*item) for item in result]
    try:
        x = 0
        while (x < len(result) - 1):
            print("%s, " % (result_list[x]), end='')
            x += 1
        print(result_list[x])
    except Exception as err:
        print(*())
