#!/usr/bin/python3
""" Script that takes in arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument
    AND is also safe from MySQL injections """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    state = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s \
                ORDER BY id", {'name': state})

    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()
