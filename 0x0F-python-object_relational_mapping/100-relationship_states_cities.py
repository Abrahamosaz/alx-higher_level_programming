#!/usr/bin/python3
"""create the database table from ORM sqlalchemy"""


def add_objects(username, password, db):
    """create both table and object entities for the database"""
    engine = create_engine("mysql+mysqldb://%s:%s@localhost:3306/%s"
                           % (username, password, db))
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_object = State(name="California")
    city_object = City(name="San Fracisco", state_id=state_object.id)
    state_object.cities.append(city_object)
    session.add(state_object)
    session.commit()


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import State, Base
    add_objects(sys.argv[1], sys.argv[2], sys.argv[3])
