# -*- coding: utf-8 -*-
import pymysql

def conn_db():
    conn = pymysql.connect(host = 'maria',
                           user = 'root',
                           password = 'qwer1234',
                           db = 'test',
                           charset = 'utf8',
                           cursorclass = pymysql.cursors.DictCursor)
    return conn

def create_table():
    conn = conn_db()
    c = conn.cursor()

    sql = '''
    create table if not exists stocks
    p_name text,
    p_qty real,
    p_price real,
    recommend text
    '''
    
    c.execute(sql)
    conn.commit()
    conn.close()
    print("테이블 생성 완료")

def insert_data():
    conn = conn_db()
    c = conn.cursor()

    name = input("상품의 이름 : ")
    qty = int(input("상품의 수량 : "))
    price = int(input("상품의 가격 : "))
    
    sql = 'insert into stocks value(%s,%s,%s)'
    c.execute(sql,[name, qty, price])
    conn.commit()
    conn.close()
    print("상품 추가 완료")

def select_data():
    conn = conn_db()
    c = conn.cursor()

    src_name = input("찾고자 하는 상품의 이름 : ")
    t = (src_name)
    sql = 'select * from stocks where p_name=%s'
    c.execute(sql, t)

    print(src_name,"의 정보 : ",end='')
    print(c.fetchall())
    conn.close()

def select_alldata():
    conn = conn_db()
    c = conn.cursor()
    c.execute("select * from stocks")

    stocks = c.fetchall()
    print(type(stocks))
    print(len(stocks))
    print(stocks)

    for stock in stocks:
        for i in stock:
            print(stock[i],end="")
        print()
    conn.close()

def update_stocks():
    conn = conn_db()
    c = conn.cursor()
    # p_name이 입력받은 값 일때 가격을 입력받은 값으로 수정
    sql = 'update stocks set price=%s where p_name=%s'
    
    cgd_name = input("가격 변경할 상품 이름 : ")
    cgd_price = input("변경할 가격 : ")
    c.execute(sql, (cgd_name, cgd_price))
    
    conn.commit()
    conn.close()
    print("가격 변경 완료")

def delete_stocks():
    conn = conn_db()
    c = conn.cursor()
    # p_name이 입력받은 값일 때 데이터 삭제
    del_name = input("삭제할 상품의 이름 : ")
    sql = 'delete from stocks where p_name=%s'
    c.execute(sql, del_name)

    print("상품 [ ",del_name," ] 삭제 완료")
    conn.commit()
    conn.close()
