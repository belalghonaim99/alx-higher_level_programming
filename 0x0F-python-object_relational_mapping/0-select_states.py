#!/usr/bin/python3

import sys
import MySQLdb
if __name__ == "__main__":
    database = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    c = database.cursor()
    c.execute("select * from 'states'")
    [print(state) for state in c.fetchall()]
