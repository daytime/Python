class Student():

    def __init__(self,name):
        self.name = name

    def calculate_avg(self,data):
        sum = 0

        for num in data:
            sum += num

        avg = sum /len(data)
        return avg

    def judge(self,avg):
        if (avg >= i):
            result = "PASSED"
        else:
            result = "FAILED"

        return result
i = 60
a001 = Student("sato")
data = [70,65,50,90,30]

avg = a001.calculate_avg(data)
result = a001.judge(avg)
print(a001.name, avg, "point")
print("avarage: ", i ,"point")
print(a001.name, result)