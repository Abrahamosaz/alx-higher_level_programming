#!/usr/bin/python3
"""fetch data from the database server"""


def fetch_cities(username, password, db):
    """function that fetch data from the database server"""
    engine = create_engine("mysql+mysqldb://%s:%s@localhost:3306/%s"
                           % (username, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    for row_data in session.query(City).order_by(City.id).all():
        print(row_data)


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    from model_state import State, Base
    fetch_cities(sys.argv[1], sys.argv[2], sys.argv[3])
