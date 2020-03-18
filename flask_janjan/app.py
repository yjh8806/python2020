# 잔잔 메뉴 홈페이지
# 1. 메뉴판 만들기
# 2. 메뉴 추가하기 (메뉴 이름, 가격, 레시피, 구입처)
# 3. 직원 추가하기
# 4. 메뉴 전체 보여주기 (메뉴 이름 클릭하면 수정,삭제,목록으로 버튼 만들기)
# 5. 메뉴 검색하기
# 6. 직원 목록
# 7. 이미지 갤러리 

from flask import Flask, request, render_template, redirect, url_for, jsonify
import pymysql, os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bootstraptest.html')

@app.route('/form')
def formTest():
    return render_template('form.html')

@app.route('/menuform', methods=['POST', 'GET'])
def menuform():
    if request.method == 'GET':
        return render_template('menuform.html')
    else:
        platename = request.form.get('platename')
        plateprice = request.form.get('plateprice')
        recipe = request.form.get('recipe')
        market = request.form.get('market')

        try:
            connection = pymysql.connect(host='maria',
                                         user='root',
                                         password='qwer1234',
                                         db='test',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
            
            with connection.cursor() as cursor:
                sql = '''
                insert into janjan values
                (%s,%s,%s,%s);
                '''
                cursor.execute(sql,(platename,plateprice,recipe,market))
                connection.coomit()

        finally:
                connection.close()

    return redirect('/list')

@app.route('/updateform/<platename>', methods=['GET'])
def updateformget():
    connection = pymysql.connect(host)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8890)