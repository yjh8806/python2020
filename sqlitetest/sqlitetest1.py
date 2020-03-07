import sqlite3

print("sqlite3 모듈 자체 버전 : ", sqlite3.version)
print("sqlite3 버전 : ", sqlite3.sqlite_version)

conn = sqlite3.connect('sqlitetest/example.db')            # 괄호안에 경로 지정
c = conn.cursor()                                          # cursor를 통해 명령 실행
c.execute('''
create table if not exists stocks
(date text, trans text, symbol text, qty real, price real)
''')                                                       # 괄호안에 실행할 Query문 입력 / SQL문 생성 시, CREATE

conn.commit()                                              # 변화가 있을 경우, commit을 해야 적용됨
conn.close()