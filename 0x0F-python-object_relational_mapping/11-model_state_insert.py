#!/usr/bin/python3
"""script that add data into the database server"""


def add_state(username, password, db):
    """add data into the database server"""
    engine = create_engine("mysql+mysqldb://%s:%s@localhost:3306/%s"
                           % (username, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    state_object = State(name="Louisiana")
    session.add(state_object)
    session.commit()
    return state_object.id


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    print(add_state(sys.argv[1], sys.argv[2], sys.argv[3]))
