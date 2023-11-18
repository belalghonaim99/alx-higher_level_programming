#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
Your script should take 3 arguments: mysql username
mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cr.fetchall()
    for i in rows:
        print(i)
    cr.close()
    db.close()
