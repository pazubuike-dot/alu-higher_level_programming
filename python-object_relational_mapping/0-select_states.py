#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL database
    # sys.argv contains: [0]script_name, [1]user, [2]password, [3]db_name
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query to get all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the executed query
    query_rows = cursor.fetchall()

    # Loop through the rows and print each one
    for row in query_rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
