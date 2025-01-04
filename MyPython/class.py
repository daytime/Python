class Student:

    def __init__(self,name):
        self.name = "none"

    def avg(self,math,english):
        print("math:",math,"english:",english,"avarage:", (math + english) / 2)

a001 = Student()
a001.avg(30,70)
a001.name = "sato"
print("name:",a001.name)
a001.gender = "male"
print("gender:",a001.gender)

a002 = Student()
# a002.name = "tanaka"
print(a002.name)