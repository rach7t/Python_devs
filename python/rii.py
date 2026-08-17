# # #wap to find the squares of number using comprehensive function 1 to 21
# squares = [x**2 for x in range(1, 22) if x%2!=0]
# print (squares)

# #wap to convert strings to uppercase
# names = ["python", "PRogramming", "laNguage"]
# uppercase_names = [name.upper() for name in names]
# print(uppercase_names)

# #wap to mark pass or fail based on marks
# marks = [85, 92, 78, 96, 88]
# results = ["Pass" if mark >= 80 else "Fail" for mark in marks]
# print(results)

# #create a list of lengths of words in a sentence
# sentence = "Python is a powerful programming language"
# word_lengths = [len(x) for x in sentence.split('p')]
# print(word_lengths)
 
# #example 
# students =[
#     ["Aman", 85],
#     ["Ravi", 92],
#     ["Priya", 78],
#     ["Anjali", 96],
#     ["Rahul", 88]
# ]
# print (students[1][1])

# #matrix
# matrix = [[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]]
# for row in matrix:
#     print("Row sum:", sum(row))


# #print number from 1 to 10 using loop
# for i in range(1, 11):
#     print(i, end="\t" )

    # #regular expression
    # import re
    # text="python programming Pythoj"
    # result = re.search(r"python", text)

# #find all the numbers in a string
# import re


# text="my roll no.is 12 and my friend roll no.is 2"
# numbers = re.findall(r"\d+", text)
# print(numbers)


# #find all the alphabets in a string
# import re
# text="RAchit is a good boy"
# alphabets = re.findall(r"[aeiouAEIOU]", text)
# print(alphabets)

#find word with exactly 5 characters
import re
text="python javascript hello world rachit"
words = re.findall(r"\w{5}", text)      
print(words)


#get date DD-MM-YYYY format
import re
text="Today is 15-03-2023"
date = re.findall(r"\d{2}-\d{2}-\d{4}", text)
print(date)