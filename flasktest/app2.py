from flask import Flask, json
from Employee import Employee

app = Flask(__name__)

@app.route("/")
def getEmployeeList():
    try:
        employeeList = []
        employeeList.append(Employee("김", "재웅"))
        employeeList.append(Employee("홍", "길동"))
        employeeList.append(Employee("이", "명희"))
        employeeList.append(Employee("박", "찬길"))
        employeeList.append(Employee("최", "호길"))
        
        jsonStr = json.dumps([e.toJSON() for e in employeeList], ensure_ascii=False, indent=4) 
        # ↑ 파이썬을 json 형태로 바꾸는 작업
        # indent -> 문장을 그냥 나열하지 않고 보기좋게 나열
    except:
        pass
    return jsonStr

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8890)