#!/usr/bin/python3
"""
Wait, do you remember the previous task?
This script is safe from MySQL injections!
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    
    # We use a %s placeholder and pass the argument as a second parameter
    # to the execute() function. The MySQLdb library handles the escaping.
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
