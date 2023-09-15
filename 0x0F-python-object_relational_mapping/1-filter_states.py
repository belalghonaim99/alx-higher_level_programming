#!/usr/bin/python3
""" Write a script that lists all states 
with a name starting with N (upper N)
from the database hbtn_0e_0_usa:"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cr.fetchall()
    for y in rows:
        print(y)
    cr.close()
    db.close()
