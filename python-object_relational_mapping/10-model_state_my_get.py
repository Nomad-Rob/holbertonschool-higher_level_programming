#!/usr/bin/python3
""" Prints the State object with name passed as arg from hbtn_0e_6_usa db """

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sesh = Session()

    try:
        state = sesh.query(State).order_by(State.id) \
                           .filter(State.name == sys.argv[4]).one()
        print(state.id)
    except Exception:
        print("Not found")
