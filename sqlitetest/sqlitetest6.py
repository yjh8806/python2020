import sqliteDB

while True:
    print('''
    1. 테이블 생성
    2. DATA 입력
    3. DATA 수정
    4. DATA 삭제
    5. DATA 목록
    6. 프로그램 종료
    ''')
    print("메뉴 선택 >>> ",end='')

    menu = input()
    print('')
    if menu == '1':
        sqliteDB.create_table()
    elif menu == '2':
        sqliteDB.insert_data()
    elif menu == '3':
        sqliteDB.update_data()
    elif menu == '4':
        sqliteDB.delete_data()
    elif menu == '5':
        sqliteDB.select_data()
    elif menu == '6':
        print("프로그램을 종료합니다")
        break
    else:
        print("메뉴를 잘못 선택하셨습니다")
