import sqlite3

conn = sqlite3.connect('New-mysite/lesson/section_12/test_sqlite.db')
# conn = sqlite3.connect(':memory:')

curs = conn.cursor()

# curs.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
# conn.commit()

# curs.execute('INSERT INTO persons(name) values("Mike")')
# conn.commit()



# curs.execute('INSERT INTO persons(name) values("Nancy")')
# curs.execute('INSERT INTO persons(name) values("Jun")')

# curs.execute('UPDATE persons set name = "Micheal" WHERE name = "Mike"')

curs.execute('DELETE FROM persons WHERE name = "Micheal"')
conn.commit()
curs.execute('SELECT * FROM persons')
print(curs.fetchall())

curs.close()
conn.close()