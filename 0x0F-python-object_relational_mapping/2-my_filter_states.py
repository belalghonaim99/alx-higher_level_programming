#!/usr/bin/python3
"""Script that takes in an argument and displays
all values in the states
table of hbtn_0e_0_usa  where name matches the argument
Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (no argument validation needed)"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cr = db.cursor()
    snMsh = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cr.execute(snMsh)
    rows = cr.fetchall()
    for i in rows:
        print(i)
    cr.close()
    db.close()
