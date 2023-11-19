#!/usr/bin/python3
"""
Write a script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
Your script should take 4 arguments: mysql username,
mysql password, database name and state name to search (SQL injection free)
You must use the module SQLAlchemy
You can assume you have one record with the state name to search
Results must display the states.id
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

    s = s.query(State).filter(State.name == argv[4]).first()
    if s:
        print("{}".format(s.id))
    else:
        print("Not found")
    s.close()
