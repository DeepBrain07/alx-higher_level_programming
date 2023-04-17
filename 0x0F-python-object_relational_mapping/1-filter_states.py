#!/usr/bin/python3

""" this script  lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa """

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySql.connect(host="localhost" user=sys.argv[1], port=3306,
                       passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    curr.execute("SELECT * FROM states")
    rows = curr.fetchall()
    for row in rows:
        if row[2][0] == 'N':
            print(row)
