from flask import Flask, render_template # import flask.Flask도 가능

app = Flask(__name__)

@app.route('/') # app 개체 생성 후 참조변수에 따라 달라질 수 있다
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8890,debug=True)