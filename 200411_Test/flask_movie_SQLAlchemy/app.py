from flask import Flask,request,render_template,redirect,url_for,jsonify,flash
import pymysql, os
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwer1234@maria/test" # mariadb 사용 시 URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # ↑ sqlite의 경우 경로 설정 -> 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)

class movie(db.Model):
    code = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    time = db.Column(db.Integer)
    sdate = db.Column(db.String(100))
    grade = db.Column(db.String(100))
    audience = db.Column(db.Integer)
    summary = db.Column(db.String(100))
    thumb = db.Column(db.String(100))

    def __init__(self, code, title, time, sdate, grade, audience, summary, thumb):
        self.code = code
        self.title = title
        self.time = time
        self.sdate = sdate
        self.grade = grade
        self.audience = audience
        self.summary = summary
        self.thumb = thumb

@app.route('/')
def index():
    return render_template('bootstraptest.html')

@app.route('/movieinfo')
def movieinfo():
    return render_template('movieinfo.html')

@app.route('/form')
def formTest():
    return render_template('form.html')

@app.route('/formresult',methods=['POST'])  
def formresult():
    username = request.form['username']
    userpass = request.form.get('userpass')
    joblist=request.form.getlist('job')
    return render_template('formresult.html',username=username,userpass=userpass,joblist=joblist) 

@app.route('/bootstrap')
def bootstraptest():
    return render_template('bootstraptest.html')

@app.route('/usersform',methods=['POST','GET'])
def usersform():
    if request.method == 'GET':
        return render_template('usersform.html')   
    else:
        #print(type(request.values))
        #for key in request.values:
        #    print(key," : ",request.values[key])
        #userid = request.form.get('userid')
        #print('userid :',userid)
        #for key in request.values:
        #    eval(str(key)+"= '"+str(request.values[key])+"'")
        userid = request.form.get('userid')
        userpw = request.form.get('userpw')
        username = request.form.get('username')
        userage = request.form.get('userage')
        useremail = request.form.get('useremail')
        useradd = request.form.get('useradd')
        usergender = request.form.get('usergender')
        usertel = request.form.get('usertel')
    
        my_user = User(userid, userpw, username, userage, useremail, useradd, usergender,usertel)
        db.session.add(my_user)
        db.session.commit()

    return redirect('/list')

@app.route('/updateform/<userid>',methods=['GET'])
def updateformget(userid):
    result = User.query.get(userid)
    return render_template('updateform.html', list = result)

@app.route('/updateform',methods=['GET', 'POST'])
def updateformpost():
    
    if request.method == 'POST':
        # id값을 통해 값을 가져와 저장해 둠
        my_user = User.query.get(request.form.get('userid'))
        
        my_user.userpw = request.form['userpw']
        my_user.username = request.form['username']
        my_user.userage = request.form['userage']
        my_user.useremail = request.form['useremail']
        my_user.useradd = request.form['useradd']
        my_user.usergender = request.form['usergender']
        my_user.usertel = request.form['usertel']
    
        db.session.commit()
        flash("업데이트 완료 !!")
        
        return redirect('/list')

@app.route('/content/<userid>')
def content(userid):
    result = User.query.get(userid)
    return render_template('content.html', list = result) 


@app.route('/deleteform/<id>')
def deleteformget(id):
    my_user = User.query.get(id)
    db.session.delete(my_user)
    db.session.commit()
    flash("회원 정보 삭제 완료 !!")
    # try:
    #     with connection.cursor() as cursor:
    #         sql="delete from users where userid = %s;"
    #         cursor.execute(sql,userid)
    #         connection.commit()
    # finally:
    #     connection.close()
    return redirect('/list')  

@app.route('/list')
def list():
    all_data = User.query.all() # 테이블 User = class User
                                # query.all() = select * from Data
    return render_template('list.html', list = all_data)

@app.route('/ajaxlist',methods=['GET'])
def ajaxlistget():
    result = User.query.all()
    return render_template('ajaxlist.html', list = result)      

@app.route('/ajaxlist',methods=['POST'])
def ajaxlistpost():
    result = User.query.filter_by(userid = '%' + User.userid + '%').all()
    # yjh8806을 y,j,h 중 꼭 y만이 아니라 다른것을 사용해서 찾을 수 있게 하려면 '%' + userid + '%'
    
    # try:
    #     with connection.cursor() as cursor:
    #             sql="select * from users where userid like %s;"
    #             userid='%' + userid+'%' 
    #             cursor.execute(sql,userid)
    #             result=cursor.fetchall()
    #             print(result)
    # finally:
    #         connection.close()
    return jsonify(result)    

@app.route('/imglist')
def imglist():
    print(os.path.dirname(__file__))
    dirname=os.path.dirname(__file__) + '/static/img/'
    filenames = os.listdir(dirname)
    print(filenames)
    return render_template('imglist.html',filenames=filenames)        

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=8890)