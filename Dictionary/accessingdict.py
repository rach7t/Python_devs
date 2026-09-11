#using []
student = {
    "name": "John",
    "age": 20,
}
print(student["name"])  # 

#using get()
student = {
    "name": "John",
    "age": 20,
}
print(student.get("name"))  # John
print(student.get("number" , "not available"))   # not available