import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('tracksdb.sqlite')
curr = conn.cursor()

# Create some fresh tables using executestrip()
curr.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fname = input('Enter your itunes xml file: ')
if (len(fname) < 1) : fname = 'Library.xml'

def lookup(d, key):
  found = False
  for child in d:
    if found : return child.text
    if child.tag == 'key' and child.text == key:
      found = True
  return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count: ', len(all))

for entry in all:
  if (lookup(entry, 'Track ID') is None) : continue
  
  name = lookup(entry, 'Name')
  artist = lookup(entry, 'Artist')
  album = lookup(entry, 'Album')
  count = lookup(entry, 'Count')
  rating = lookup(entry, 'Rating')
  length = lookup(entry, 'Total Time')
  genre = lookup(entry, 'Genre')

  if name is None or artist is None or album is None or genre is None :
    continue

  #print(name, artist, album, count, rating, length, genre)
  curr.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist,))
  curr.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
  artist_id = curr.fetchone()[0]
  curr.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
                  VALUES (?, ?)''', (album, artist_id))
  curr.execute('''SELECT id FROM Album WHERE title = ?''', (album, ))
  album_id = curr.fetchone()[0]
  curr.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre,))
  curr.execute('SELECT id FROM Genre WHERE name=?', (genre,))
  genre_id = curr.fetchone()[0]

  curr.execute('''INSERT OR REPLACE INTO Track
          (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)''',
          (name, album_id, genre_id, length, rating, count))


conn.commit()

sqlstr = '''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3'''

for row in curr.execute(sqlstr):
  print(row[0], row[1], row[2], row[3])

curr.close()