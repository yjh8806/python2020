import productDB

while True:
    print('''
    1. 상품 테이블 생성
    2. 상품 입력
    3. 상품 수정
    4. 상품 삭제
    5. 상품 정보
    6. 상품 전체 목록
    7. 프로그램 종료
    ''')
    print("메뉴 선택 >>> ")

    menu = input()
    print('')
    if menu == '1':
        productDB.create_table()
    elif menu == '2':
        productDB.insert_data()
    elif menu == '3':
        productDB.update_stocks()
    elif menu == '4':
        productDB.delete_stocks()
    elif menu == '5':
        productDB.select_data()
    elif menu == '6':
        productDB.select_alldata()
    elif menu == '7':
        print("프로그램을 종료합니다")
        break
    else:
        print("메뉴를 잘못 선택하셨습니다")
