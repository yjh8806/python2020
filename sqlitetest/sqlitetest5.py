# csv -> db
import sqlite3, csv     # 라이브러리 csv


conn = sqlite3.connect('sqlitetest/sup.db')
cur = conn.cursor()

sql =   '''
        create table if not exists sup
        (
            sup_name varchar(20), 
            invoice_number varchar(20),
            part_number varchar(20),
            cost float,
            date date
        )
        ''' # date = 날짜형

cur.execute(sql)

sql = 'delete from sup'
cur.execute(sql)

input_file = 'sqlitetest/input.csv'
open_file = open(input_file, 'r')
file_reader = csv.reader(open_file, delimiter = ',') # default = ','
print(next(file_reader))                             # 상황에 따라 구분자 delimiter 지정
                                                     # Next는 첫번째 줄 제목을 리스트에 넣지 않기위해 다음으로 넘김
data = []
for row in file_reader:
    data.append(row)

sql = 'insert into sup values(?,?,?,?,?)'
cur.executemany(sql, data)
conn.commit()
conn.close()