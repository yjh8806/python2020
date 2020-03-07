import sqlite3

conn = sqlite3.connect('sqlitetest/example.db')
c = conn.cursor()

data = [
    ('2020-01-05', 'buy', 'rhat', 200, 24.31),
    ('2020-02-17', 'buy', 'com', 100, 9.74),
    ('2020-05-27', 'buy', 'net', 55, 56.1),
    ('2020-06-08', 'buy', 'com', 42, 17.67)
    ]

sql = 'insert into stocks values(?,?,?,?,?)'
c.executemany(sql, data)

conn.commit()
conn.close()