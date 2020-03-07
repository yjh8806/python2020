import sqlite3

def db_conn():
    return sqlite3.connect('sqlitetest/book.db')
    
def create_table():
    conn = db_conn()
    cur = conn.cursor()
    sql = '''
    create table if not exists books (
        title       text,
        pub_date    text,
        pub         text,
        pages       integer,
        recommend   integer
    )
    '''

    cur.execute(sql)
    conn.commit()
    conn.close()
    print("테이블 생성 완료 !")

def insert_data():
    conn = db_conn()
    cur = conn.cursor()
    title = input("책 제목 : ")
    pub_date = input("출판일(""-""로 구분) : ")
    pub = input("출판사 : ")
    pages = int(input("총 페이지 수 : "))
    recommend = input("비고 : ")
    
    data = [title, pub_date, pub, pages, recommend] # 원하는 형태로
    sql = 'insert into books values(?,?,?,?,?)'

    cur.execute(sql, data)
    conn.commit()
    conn.close()

def select_data():
    conn = db_conn()
    cur = conn.cursor()
    title = input("찾는 책의 제목 : ")
    title = '%' + title + '%'   # 책 제목의 일부만 입력해도 출력 가능
                                # '_' : 글자숫자를 정해줌(ex) 컬럼명 like 홍_동)
                                # '%' : 글자숫자를 정해 주지 않음(ex) 컬럼명 like '홍%')
    sql = 'select * from books where title like ?'
    cur.execute(sql, (title,))  # 튜플은 구분자 ','로

    print("현재 DATA 목록")
    print(">>> ",end='')
    print(cur.fetchall())
    conn.close()
    # 전체 목록을 출력하려면 title 변수 작업 필요 X

def select_alldata():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('select * from books')

    print("현재 DATA 목록")
    print(">>> ",end='')
    print(cur.fetchall())
    conn.close()
    # 전체 목록을 출력하려면 title 변수 작업 필요 X


def update_date():
    pass

def delete_data():
    pass
