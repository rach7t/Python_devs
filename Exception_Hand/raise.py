# raise ZeroDivisionError("ABCD")
# x = 5
# y = 8
# if x>y:
#     raise ZeroDivisionError("ABCD")
# else:
#     print("x is less than y")

class FiveDivisionError(Exception):
    pass

l = [1,2,3,4,5,6,7,8,8,9,10]
for i in l:
    if i%5==0:
      try:
            raise FiveDivisionError("This number is divisible by 5")
      except FiveDivisionError as e:
            print(e)
    else:
        print("No number is  not divisible by 5")

class Student:
    pass