import sqlite3

# Make connection
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Drop table if it exists
cur.execute('DROP TABLE IF EXISTS Counts')

# Create table named Counts in db
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')