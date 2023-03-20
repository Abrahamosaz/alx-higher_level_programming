#!/usr/bin/python3
"""retrieve data from cities and states tables from database server"""


def get_data(username, password, db):
    """get data from cities and states tables from the database"""
    engine = create_engine("mysql+mysqldb://%s:%s@localhost:3306/%s"
                           % (username, password, db))

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).join(
            City, State.id == City.state_id
            ).order_by(State.id, City.id).all()
    for state in result:
        print("%d: %s" % (state.id, state.name))
        for city in state.cities:
            print("\t", end="")
            print("%d: %s" % (city.id, city.name))


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import State
    get_data(sys.argv[1], sys.argv[2], sys.argv[3])
