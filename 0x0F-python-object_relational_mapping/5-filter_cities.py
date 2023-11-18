#!/usr/bin/python3
"""
Your script should take 4 arguments: mysql username,
mysql password, database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cr = db.cursor()
    cr.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])
    rows = cr.fetchall()
    c = []
    for i in rows:
        c.append(i[1])
    print(", ".join(c))
    cr.close()
    db.close()
