def display_student(*name,**kwargs):
    print(name)
    for key,value in kwargs.items():
        print(key,":",value)

def display(*args,**kwargs):
    print("positional arguments:",args)
    print("keyword arguments:",kwargs)

display(10,20,30,name="Neha",branch="cse")