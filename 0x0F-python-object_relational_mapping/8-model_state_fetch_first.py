#!/usr/bin/python3
"""retrieve data from the database server"""


def retrieve_first_data(username, password, db):
    """function that print the first row data in the database"""
    engine = create_engine("mysql+mysqldb://%s:%s@localhost:3306/%s"
                           % (username, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    first_row = session.query(State).order_by(State.id).first()
    print("%s: %s" % (first_row.id, first_row.name))


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    retrieve_first_data(sys.argv[1], sys.argv[2], sys.argv[3])
