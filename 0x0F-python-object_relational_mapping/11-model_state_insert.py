#!/usr/bin/python3
"""
 script that adds the State object
 “Louisiana” to the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session_maker = sessionmaker(bind=engine)
    sess = Session_maker()
    Base.metadata.create_all(engine)

    add_state = State(name="Louisiana")
    sess.add(add_state)
    sess.commit()
    print(add_state.id)
    sess.close()
