class Student:
    pass

s1 = Student()
s2 = Student()
s1.rollno=123
s1.branch="cse-aiml"
s1.name="ravi"
print(s1.__dict__)
s2.rollno=456
print(s2.__dict__)