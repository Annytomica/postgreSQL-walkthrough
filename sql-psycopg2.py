import psycopg2

# connect to 'chinook' database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database - where queries get stored
cursor = connection.cursor()

## This is where all queries go
## IMPORTANT: Use '' to wrap query and "" to wrap database values

# Query 1 - select all records from the 'artist' table
#cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table - can be done with .fetchone()
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" from the "Artist" table - can be done with .fetchone()
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', ["51"])

# Query 5 - select only the album with "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', ["51"])

# Query 6 - select all tracks where composer is "Queen" form the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - test what happens if composer not in database
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Test"])

## These are the functions to use for queries (multiple and single)

# fetch the query results (multiple) from the cursor object
results = cursor.fetchall()

# fetch a query result (single) from the cursor object
# results = cursor.fetchone()

# close the connection to database
connection.close()

# print results
for result in results:
    print(result)