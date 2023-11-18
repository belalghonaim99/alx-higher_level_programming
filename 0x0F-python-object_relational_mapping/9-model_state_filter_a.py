#!/usr/bin/python3
"""Write a script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state
from model_state import Base, State
Results must be sorted in ascending order by states.id"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    e = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                      .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                      pool_pre_ping=True)
    Session_maker = sessionmaker(bind=e)
    s = Session_maker()

    for state in s.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
