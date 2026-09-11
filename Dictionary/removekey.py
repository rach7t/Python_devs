#pop
student = {
    "name": "John",
    "age": 20
}
student.pop("age")
print(student)  # {'name': 'John'}

#popitem
student = {
    "name": "John",
    "age": 20
}
print(student.popitem())  # ('age', 20) 

#clear
student = {
    "name": "John",
    "age": 20
}
print(student.clear())  # None

#del
student = {
    "name": "John",
    "age": 20
}
