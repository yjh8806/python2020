import pymysql

conn = pymysql.connect(host='maria',
                        user='root',
                        password='qwer1234',
                        db='test',
                        charset='utf8')

c=conn.cursor()

data=[
    ('2020-02-01','buy','com',200,5.14),
    ('2020-02-02','buy','net',100,3.14),
    ('2020-02-03','buy','rhat',50,35.1),
    ('2020-02-04','buy','com',42,305.14)
    ]

sql='insert into stocks values(%s,%s,%s,%s,%s)'

c.executemany(sql,data)
conn.commit()
sql='select * from stocks order by price desc'
c.execute(sql)
print(c.fetchall())
conn.close()