#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Session_maker = sessionmaker(bind=eng)
    sess = Session_maker()

    louisiana = State(name="Louisiana")
    sess.add(louisiana)
    sess.commit()
    print(louisiana.id)
