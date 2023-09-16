#!/usr/bin/python3
"""Python file similar to model_state.py named model_city.py
that contains the class definition of a City."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Session_maker = sessionmaker(bind=eng)
    sess = Session_maker()

    for city, state in sess.query(City, State) \
            .filter(City.state_id == State.id) \
            .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
