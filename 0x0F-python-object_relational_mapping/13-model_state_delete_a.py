#!/usr/bin/python3
"""
script that deletes all State objects
with a name containing the letter
a from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session_maker = sessionmaker(bind=eng)
    sess = Session_maker()
    Base.metadata.create_all(eng)
    state_delete = sess.query(State).filter(State.name.like('%a%')).all()
    for delete in state_delete:
        sess.delete(delete)
    sess.commit()
    sess.close()
