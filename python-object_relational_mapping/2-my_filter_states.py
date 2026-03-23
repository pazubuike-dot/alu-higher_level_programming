#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
Safe from MySQL injection is NOT required for this specific task.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to database using 3 arguments
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    
    # Use format to create the SQL query with the user input (sys.argv[4])
    # The BINARY keyword ensures exact case-sensitive matching
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
             ORDER BY id ASC".format(sys.argv[4])
    
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
