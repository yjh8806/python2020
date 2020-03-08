import pymysql

conn = pymysql.connect(host = 'maria',
                       user = 'root',
                       password = 'qwer1234',
                       db = 'test',
                       charset = 'utf8')

c = conn.cursor()

data = data = [
    ('2020-01-05', 'buy', 'rhat', 200, 24.31),
    ('2020-02-17', 'buy', 'com', 100, 9.74),
    ('2020-05-27', 'buy', 'net', 55, 56.1),
    ('2020-06-08', 'buy', 'com', 42, 17.67)
    ]

sql = ('insert into stocks values(%s,%s,%s,%s,%s)')

c.executemany(sql, data)
conn.commit()   # insert문은 변화 有! commit 필수

sql = ('select * from stocks order by price desc') # order by ~~: ~~순으로 정렬
c.excute(sql)
print(c.fetchall())
conn.close()
