#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to a MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query with BINARY to force case sensitivity
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                   ORDER BY id ASC")

    # Fetch all the rows from the executed query
    query_rows = cursor.fetchall()

    # Loop through the rows and print each one
    for row in query_rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
