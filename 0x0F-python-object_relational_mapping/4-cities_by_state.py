#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cr = db.cursor()
    cr.execute("SELECT `ci`.`id`, `ci`.`name`, `st`.`name` \
                 FROM `cities` as `ci` \
                INNER JOIN `states` as `st` \
                   ON `ci`.`state_id` = `st`.`id` \
                ORDER BY `ci`.`id`")
    [print(city) for city in cr.fetchall()]