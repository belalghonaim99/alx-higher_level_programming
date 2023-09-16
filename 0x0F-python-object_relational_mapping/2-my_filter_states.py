#!/usr/bin/python3
"""Script that takes in an argument and displays
all values in the states
table of hbtn_0e_0_usa  where name matches the argument"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cr = db.cursor()
    sNmSh = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cr.execute(sNmSh)
    rows = cr.fetchall()
    for y in rows:
        print(y)
    cr.close()
    db.close()