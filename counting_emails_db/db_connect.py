import sqlite3

# Make connection
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Drop table if it exists
cur.execute('DROP TABLE IF EXISTS Counts')

# Create table named Counts in db
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Prompt user for file if no file provided use fallback
fname = input('Enter file name to parse: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
# Loop through the lines in file
count = 1
for line in fh:
  # skip line if line is not starting with From:
  if not line.startswith('From: '): continue
  pieces = line.split()
  domain = pieces[1].split('@')[1]
  # Checking for presence of certain domain
  cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
  # Getting first row from all the query results
  row = cur.fetchone()
  if row is None:
    cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (domain,))
  else:
    cur.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''', (domain,))
  # Commit query
  
  count += 1
  print('Still working... on entry nr.: ', count)
# Slow when inside a loop because of the update statment
conn.commit()
# Select from db top 10 domains that emailed and sort desc by count
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
  print(str(row[0]), row[1])

cur.close()