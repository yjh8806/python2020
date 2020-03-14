import pymysql

conn = pymysql.connect(host='maria',
                        user='root',
                        password='qwer1234',
                        db='test',
                        charset='utf8')

c=conn.cursor()
symbol=input('심볼을 입력하세요')
sql="select * from stocks where symbol=%s"
c.execute(sql,symbol)
print(c.fetchall())
conn.close()