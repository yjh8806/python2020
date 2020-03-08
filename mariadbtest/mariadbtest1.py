import pymysql

conn = pymysql.connect(host = 'maria',
                       user = 'root',
                       password = 'qwer1234',
                       db = 'test',
                       cursorclass = pymysql.cursors.DictCursor)

c = conn.cursor()
c.execute('''
create table if not exists stocks
(date text, trans text, symbol text, qty real, price real)
''')

c.execute('''
insert into stocks
values('2020-01-05', 'buy', 'rhat', 100, 35.14)
''')

conn.commit() # c.execute()에서 변화(insert)가 있었으므로, commit()해주어야 함
conn.close()