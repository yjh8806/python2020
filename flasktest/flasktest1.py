from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>') # <name> --> 넘어오는 데이터 값
def hello(name = None):
    if name is None:
        return 'A horse with no name'
    else:
        return 'A horse me named %s'%name

@app.route('/login' , methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        return render_template('list.html', data=request.form) # return request.form['Name']
    else:
        return "get"

@app.route('/list/<name>')
def listdata(name):
    return name

@app.route('/form/')
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8890)