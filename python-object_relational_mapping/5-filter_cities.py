#!/usr/bin/python3
""" Lists all cities of a given state from the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    
    # Safe query using %s for the state name
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    
    # We need to print names separated by commas (e.g., Dallas, Houston, Austin)
    # Extract names from tuples and join them
    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()
