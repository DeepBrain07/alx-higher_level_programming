#!/usr/bin/python3

""" this script takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument. """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    curr = db.cursor()
    curr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(argv[4]))
    rows = curr.fetchall()
    for row in rows:
        print(row)
