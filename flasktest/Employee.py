class Employee():
    def __init__(self, firstName, lastName): # 지역변수 firstName, lastName
        self.firstName = firstName           # 지역변수를 전역변수로 바꾸는 작업
        self.lastName = lastName

    def toJSON(self):
        return {"emp" : {'firstName' : self.firstName,
                         'lastName' : self.lastName}}