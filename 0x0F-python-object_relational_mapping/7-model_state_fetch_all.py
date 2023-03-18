#!/usr/bin/python3
"""using sqlalchemy to retrieve data from the database"""


def retrieve_data(username, password, db):
    """function to retrieve data from the database server"""
    engine = create_engine("mysql+mysqldb://%s:%s@localhost:3306/%s"
                           % (username, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State).order_by(State.id).all():
        print("{}: {}".format(row.id, row.name))


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State
    import sys
    retrieve_data(sys.argv[1], sys.argv[2], sys.argv[3])
