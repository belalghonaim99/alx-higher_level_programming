#!/usr/bin/python3
"""
Write a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username,
mysql password and database name
Print the new states.id after creation
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    e = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session_maker = sessionmaker(bind=e)
    s = Session_maker()
    Base.metadata.create_all(e)

    add_state = State(name="Louisiana")
    s.add(add_state)
    s.commit()
    print(add_state.id)
    s.close()
