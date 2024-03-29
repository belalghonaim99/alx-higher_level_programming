#!/usr/bin/python3
"""
a script that changes the name of a State object
from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
Your script should connect to a MySQL server running on localhost at port 3306
Change the name of the State where id = 2 to New Mexico
"""
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

    state = s.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    s.commit()
