#!/usr/bin/python3
"""retrieve data from the database server"""


def like_data(username, password, db):
    """function that print row data that contain the letter a"""
    engine = create_engine("mysql+mysqldb://%s:%s@localhost:3306/%s"
                           % (username, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    for row_data in session.query(State).order_by(State.id).filter(
            text("states.name LIKE '%a%'")
            ).all():
        print("%s: %s" % (row_data.id, row_data.name))


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import text
    from model_state import State, Base
    like_data(sys.argv[1], sys.argv[2], sys.argv[3])
