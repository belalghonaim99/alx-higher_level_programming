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
    e = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session_maker = sessionmaker(bind=e)
    s = session_maker()
    Base.metadata.create_all(e)

    city = s.query(State, City).join(City).order_by(City.id)
    for s, city in city:
        print("{}: ({}) {}".format(s.name, city.id, city.name))
    s.close()