#!/usr/bin/python3
"""delete all state object contain the letter a in the database server"""


def delete_state(username, password, db):
    """delete state object that contain the letter a"""
    engine = create_engine("mysql+mysqldb://%s:%s@localhost:3306/%s"
                           % (username, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    instances = session.query(State).filter(
            text("states.name LIKE '%a%'")
            ).all()
    for instance in instances:
        session.delete(instance)
    session.commit()


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    delete_state(sys.argv[1], sys.argv[2], sys.argv[3])
