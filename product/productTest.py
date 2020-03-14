import productF

while True:
    print('''
    1. 상품 테이블 생성
    2. 상품 추가
    3. 상품 목록
    4. 상품 전체 목록
    5. 상품 수정
    6. 상품 삭제
    7. 프로그램 종료
    메뉴선택 >> ''')

    menu=input()
    if menu=='1':
        productF.create_table()
    elif menu=='2':
        productF.insert_data()
    elif menu=='3':
        productF.select_data()
    elif menu=='4':
        productF.select_alldata()
    elif menu=='5':
        productF.update_stocks()
    elif menu=='6':
        productF.delete_stocks()
    elif menu=='7':
        print("프로그램을 종료합니다")
        break
    else:
        print("메뉴를 잘못 선택하셨습니다")
