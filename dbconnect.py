import sqlite3

try:

    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('library.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Write a query and execute it with cursor
    query = 'select * from customers'
    cursor.execute(query)
 
    # insert = """INSERT INTO customers (ID, NAME,email,address)VALUES ('2', 'Paul2', 'pra2@gmail.com', 'California')"""
    # cursor.execute(insert)

    # Fetch and output result
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))

    # cursor.commit()

    # Close the cursor
    cursor.close()

# Handle errors
except sqlite3.Error as error:
    print('Error occurred - ', error)

# Close DB Connection irrespective of success
# or failure
finally:

    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')
