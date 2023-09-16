#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_us"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cr = db.cursor()
    cr.execute("SELECT * FROM `cities` as `ci` \
                INNER JOIN `states` as `st` \
                   ON `ci`.`state_id` = `st`.`id` \
                ORDER BY `ci`.`id`")
    print(" , ".join([ci[2] for ci in cr.fetchall() if ci[4] == sys.argv[4]]))