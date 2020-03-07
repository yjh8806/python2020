import sqlite3

conn = sqlite3.connect('python2020/sqlitetest/example.db')
c = conn.cursor()
c.execute('''
insert into stocks
values('2020-01-05', 'buy', 'rhat', 100, 35.14)
''') # insert into 테이블명 values()

conn.commit() # c.execute()에서 변화가 있었으므로, commit()해주어야 함
conn.close()