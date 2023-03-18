#!/usr/bin/python3
"""retrieve data from the database server"""


def get_state_id(username, password, db, state_name):
    """function that return the id of the state found base on the command
    line argument passed to the function"""
    engine = create_engine("mysql+mysqldb://%s:%s@localhost:3306/%s" %
                           (username, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    for row_data in session.query(State).all():
        if row_data.name == state_name:
            return row_data.id
    return "Not found"


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    print(get_state_id(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
