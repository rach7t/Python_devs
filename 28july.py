s='Rachit Paliwal'



#wap to accept first name and last name and print full name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print(f'Full name: {full_name}')

#wap to print a star pattern using for loop
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i + 1):
        print("*", end="")
    print()

#wap to show strips and use strips function
str1 = "   Hello, World! Hello Hello Hello    "
print(f'Original string: "{str1}"')
print(f'Left stripped: "{str1.lstrip()}"')
print(f'Right stripped: "{str1.rstrip()}"')
print(f'Both stripped: "{str1.strip()}"')
print(str1.replace("Hello","hi",2))


#wap to get username(alphabet only )  age (Digits only ) course (Title case) And Dispaly wheather the each input is valid or not
 

