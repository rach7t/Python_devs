class Student:
    def __init__(self):
        print ("no-arg")

    def __init__(ab,rn,n,b):
        print("parameterized")
        ab.rollno=rn
        ab.name=n
        ab.branch=b

s0=Student()
s1=Student(123,"ravi","cse-aiml")
s2=Student(456,"ramesh","cse-aiml")