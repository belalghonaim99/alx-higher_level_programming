#!/usr/bin/python3
"""script that changes the name of a State
object from the database hbtn_0e_6_usa
Change the name of the State where id = 2 to New Mexico
"""
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

    state = sess.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    sess.commit()
