#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa
Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id"""
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