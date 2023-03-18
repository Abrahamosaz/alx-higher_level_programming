#!/usr/bin/python3
"""update the row data in the database server"""


def update_state(username, password, db):
    """update the row data in the database server"""
    engine = create_engine("mysql+mysqldb://%s:%s@localhost:3306/%s"
                           % (username, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    state_object = session.query(State).filter(text("states.id = 2")).scalar()
    state_object.name = "New Mexico"
    session.commit()


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    update_state(sys.argv[1], sys.argv[2], sys.argv[3])
