import pymysql

conn = pymysql.connect(host='maria',
                        user='root',
                        password='qwer1234',
                        db="test",
                        charset='utf8',
                        cursorclass=pymysql.cursors.DictCursor
                        )

c=conn.cursor()

sql='select * from stocks'

c.execute(sql)

print(c.fetchall())

conn.close()