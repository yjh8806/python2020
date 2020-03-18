import pymysql

connection = pymysql.connect(host='maria',
                             user = 'root',
                             password = 'qwer1234',
                             db = 'test',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = '''
        drop table if exists janjan;
        '''
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        sql = '''
        drop table if exists employee;
        '''
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        # 잔잔 메뉴 홈페이지
        # 1. 메뉴판 만들기
        # 2. 메뉴 추가하기 (메뉴 이름, 가격, 레시피, 구입처)
        # 3. 직원 추가하기 (직원 번호, 이름, 나이, 연락처)
        # 4. 메뉴 전체 보여주기 (메뉴 이름 클릭하면 수정,삭제,목록으로 버튼 만들기)
        # 5. 메뉴 검색하기
        # 6. 직원 목록
        # 7. 이미지 갤러리 
        sql = '''
        create table if not exists janjan
        (
        platename varchar(20) primary key,
        plateprice int,
        recipe varchar(1000),
        market varchar(50)
        );
        '''
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        sql = '''
        create table if not exists employee
        (
        usernum varchar(20) primary key,
        username varchar(20) not null,
        userage int,
        usertel varchar(20)
        );
        '''
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        sql = '''
        insert into janjan values
        (
        '나가사키 짬뽕',15000,'1. 야채준비,볶기,끓이기,담기','야채 - 엄궁시장, 면 - 모노마트'
        );
        '''
        cursor.execute(sql)
        connection.commit()
    
    with connection.cursor() as cursor:
        sql = '''
        insert into employee values
        (
        '1','윤정현',27,'010-8806-5438'
        );
        '''
        cursor.execute(sql)
        connection.commit()
    
    with connection.cursor() as cursor:
        sql = '''
        select * from janjan;
        '''
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    
    with connection.cursor() as cursor:
        sql = '''
        select * from employee;
        '''
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    connection.close()