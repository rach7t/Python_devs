

#calculate the sum of numbers from 1 to 10 using while loop
sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
print(f"Sum of numbers from 1 to 10: {sum}")

#calculate the sum of digits in a number using while loop
x = 12345
sum_of_digits = 0
while x > 0:
    digit = x % 10
    sum_of_digits += digit
    x //= 10
print(f"Sum of digits in 12345: {sum_of_digits}")
#wap that print all the numbers from 0 to 6 except 3 and 6 
i = 0
while i <= 6:
    if i==3 or i==6:
        i += 1
        continue
    print(i)
    i += 1

#wap to check whether a number is armstrong number or not
num = 153
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")


#wap to check fibonacci series using while loop
a = 0
b = 1
print(a, b, end=" ")
i = 2
while i < 10:
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    i += 1