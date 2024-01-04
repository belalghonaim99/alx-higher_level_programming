#!/usr/bin/python3
"""
Write a script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
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
    state_delete = s.query(State).filter(State.name.like('%a%')).all()
    for delete in state_delete:
        s.delete(delete)
    s.commit()
    s.close()
