#!/usr/bin/python3
""" Adds 'Louisiana' to hbtn_0e_6_usa db """

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sesh = Session()

    sesh.add(State(name="Louisiana"))

    new_state = sesh.query(State).filter(State.name == "Louisiana").first()
    print(f'{new_state.id}')

    sesh.commit()
