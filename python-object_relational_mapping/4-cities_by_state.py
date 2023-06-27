#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states ON cities.state_id = states.id")
    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
