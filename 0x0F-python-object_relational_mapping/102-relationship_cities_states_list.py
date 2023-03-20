#!/usr/bin/python3
"""script that retrieve data from the database server"""


def get_cities(username, password, db):
    """get the cities object and states associated with the city object"""
    engine = create_engine("mysql+mysqldb://%s:%s@localhost:3306/%s"
                           % (username, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City).order_by(City.id).all():
        print("%d: %s -> %s" % (city.id, city.name, city.state.name))


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    get_cities(sys.argv[1], sys.argv[2], sys.argv[3])
