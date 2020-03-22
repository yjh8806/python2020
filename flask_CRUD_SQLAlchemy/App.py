from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwer1234@maria/test" # mariadb 사용 시 URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # ↑ sqlite의 경우 경로 설정 -> 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)

#---------------------------------테이블 정의
#Creating model table for our CRUD database
class Data(db.Model): # 테이블 만드는 작업 (class를 통해서)
                      # Data가 테이블 이름
                      # id,name,email,phone : 필드 생성
                      # (sql 쿼리문 create와 비교)
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    # id 입력안해도 자동으로 
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
#---------------------------------테이블 정의


#This is the index route where we are going to
#query on all our employee data
@app.route('/')
def Index():
    all_data = Data.query.all() # 테이블 Data = class Data
                                # query.all() = select * from Data
    return render_template("index.html", employees = all_data)



#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']


        my_data = Data(name, email, phone) # 데이터 개체 생성(my_data)
        db.session.add(my_data)            # 추가하고
        db.session.commit()                # commit()까지

        flash("Employee Inserted Successfully")

        return redirect(url_for('Index'))


#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
                # id값을 통해 값을 가져와 저장해둠
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']

        db.session.commit()
        flash("Employee Updated Successfully")
        
        return redirect(url_for('Index'))


#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='8890')