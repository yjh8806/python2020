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

