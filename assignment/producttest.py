# -*- coding: utf-8 -*-
import productDB

while True:
    print('''
    1. 상품 테이블 생성
    2. 상품 입력
    3. 상품 수정
    4. 상품 삭제
    5. 상품 목록
    6. 상품 전체 목록
    7. 프로그램 종료
    ''')
    print("메뉴 선택 >>> ")

    menu = input()
    print('')
    if menu == '1':
        productDB.create_table()
    elif menu == '2':
        pass
    elif menu == '3':
        pass
    elif menu == '4':
        pass
    elif menu == '5':
        pass
    elif menu == '6':
        pass
    elif menu == '7':
        print("프로그램을 종료합니다")
        break
    else:
        print("메뉴를 잘못 선택하셨습니다")
