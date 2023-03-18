#!/usr/bin/python3
"""retrieve data from database safe from sql injection query"""


def safe_match_states(username, password, db, state_string):
    """function that return data base on the state string safe
    from sql injection query syntax"""
    db_engine = MySQLdb.connect(
            host="localhost",
            user=username,
            password=password,
            database=db
            )
    conn = db_engine.cursor()
    conn.execute("SELECT * FROM states WHERE name=%s", (state_string,))
    return conn.fetchall()


if __name__ == "__main__":
    import MySQLdb
    import sys
    result = safe_match_states(sys.argv[1], sys.argv[2],
                               sys.argv[3], sys.argv[4])
    for data in result:
        print(data)
