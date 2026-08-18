#wap to to input a string and display it 
str = input("Enter a string: ")
print("You entered:", str)



#wap to input a string and find the length of it without using len() function
str = input("enter a string:")
length = 0
for char in str:
    length += 1
print("Length of the string:", length)

#wap to convert a string to uppercase and lowercase
str = input("Enter a string: ")
print("Uppercase:", str.upper())
print("Lowercase:", str.lower())


#wap to count number of vowels and consonant in a string 
str = input("enter a string:")
vowels = 0
cons =0 
for char in str:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            cons += 1
print("Number of vowels:", vowels)
print("Number of consonants:", cons)