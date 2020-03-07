import sqlite3

conn = sqlite3.connect('sqlitetest/example.db')
c = conn.cursor()

c.execute('select * from stocks') # * -> 와일드카드, 모든 것

print(c.fetchone())               # select의 경우 insert처럼 commit필요 X 대신 fetch 필요
print(c.fetchmany(3))             # fetchone, fetchall 이후 fetchmany출력하면 리스트가 비어있음
print(c.fetchall())

symbol = input("심볼을 입력하세요 : ")
sql = "select * from stocks where symbol = '%s'" %symbol
sql = "select * from stocks where symbol = ?"

c.execute(sql, [symbol])          # symbol 리스트는 []
# c.execute(sql, (symbol,))         symbol 튜플형인 경우 ','로 구분

print(c.fetchall())
conn.close()                      # commit은 필요 X, But close()는 해줘야 함