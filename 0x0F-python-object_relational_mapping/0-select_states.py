#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    dbs = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cr = dbs.cursor()
    cr.execute("SELECT * FROM states")

    rows = cr.fetchall()
    for y in rows:
        print(y)
    cr.close()
    dbs.close()
