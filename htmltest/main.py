from flask import Flask, render_template
app = Flask(__name__)

@app.route('/info')
def index():
    return 'Hello Flask'
    
@app.route('/')
def info():
     return render_template('index.html')

if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8890",debug=True)