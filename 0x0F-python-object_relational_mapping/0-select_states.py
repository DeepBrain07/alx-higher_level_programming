#!usr/bin/python3
""" This script lists all states from the database hbtn_0e_0_usa """

import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    curr.execute("SELECT  * FROM 'states' ORDER BY 'states.id' ASC")
