#!/usr/bin/python3
""" script that deletes all State objects with a
name containing the letter a from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session_maker = sessionmaker(bind=eng)
    sess = Session_maker()

    for state in sess.query(State):
        if "a" in state.name:
            sess.delete(state)
    sess.commit()
