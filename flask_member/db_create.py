import pymysql
connection = pymysql.connect(host = 'maria',
                             user = 'root',
                             password = 'qwer1234',
                             db = 'test',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor) # cursorclass 지정 없으면 결과값은 리스트로 출력
                                                                       # << 현재는 딕셔너리 형태이므로 key값으로 접근 !! >>

try:
    with connection.cursor() as cursor: # connection.cursor()를 cursor로 사용하겠다. EX) cursor.excute()
        sql ='''
        drop table if exists users; 
        '''
        cursor.execute(sql)
        connection.commit()             # 넣고 지우고 수정하는 모든 행위는 commit()

    with connection.cursor() as cursor:
        sql = '''
        create table if not exists users
        (   userid varchar(20) primary key,
            userpw varchar(20) not null,
            username varchar(20) not null,
            userage int,
            useremail varchar(20),
            useradd varchar(50),
            usergender varchar(20),
            usertel varchar(20)
        );
        '''
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        sql = '''
        insert into users values
        ('hong','1234','홍길동',23,'hong@gmail.com','부산시 동구 수정동','male','010-1234-1234');
        '''
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        sql = '''
        select * from users;
        '''
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    connection.close()