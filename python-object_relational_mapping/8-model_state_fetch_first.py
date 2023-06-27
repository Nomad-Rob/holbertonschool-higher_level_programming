#!/usr/bin/python3
""" Lists all states in the states table """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sesh = Session()
    first_state = sesh.query(State).first()
    if first_state:
        print(f'{first_state.id}: {first_state.name}')
    else:
        print("Nothing")
