from flask import Flask, request, render_template, redirect, url_for, jsonify
import pymysql, os # os : 경로 필요하기 때문에 import

app = Flask(__name__)

@app.route('/') # / : 홈으로 접속
def index():
    return render_template('bootstraptest.html')





















if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 8890)