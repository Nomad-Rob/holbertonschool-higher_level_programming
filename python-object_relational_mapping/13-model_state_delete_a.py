#!/usr/bin/python3
""" Deletes all State objects with name containing 'a' in hbtn_0e_6_usa db """

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sesh = Session()

    for row in sesh.query(State).filter(State.name.contains('a')):
        sesh.delete(row)

    sesh.commit()
