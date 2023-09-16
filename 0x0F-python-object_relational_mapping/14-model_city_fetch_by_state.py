#!/usr/bin/python3
"""
Python file similar to model_state.py
named model_city.py that contains
the class definition of a City.
"""
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    sess = session_maker()
    Base.metadata.create_all(engine)

    c = sess.query(State, City).join(City).order_by(City.id)
    for s, c in c:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    sess.close()
