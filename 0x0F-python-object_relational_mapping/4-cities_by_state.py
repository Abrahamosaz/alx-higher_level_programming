#!/usr/bin/python3
"""retrieve all cities from the database server"""


def list_cities(username, password, db):
    """function that take commnad line argument and retrieve
    data from the mysql server database"""
    db_engine = MySQLdb.connect(
            host="localhost",
            user=username,
            password=password,
            database=db
            )
    conn = db_engine.cursor()
    conn.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities INNER JOIN states ON states.id = \
                 cities.state_id ORDER BY cities.id")
    return conn.fetchall()


if __name__ == "__main__":
    import MySQLdb
    import sys
    result = list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
    for data in result:
        print(data)
