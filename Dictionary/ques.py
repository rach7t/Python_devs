#create a dictionary with some key-value pairs of numbers and their squares using dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print("Dictionary of numbers and their squares:", squares_dict)


#wap to convert a list of words in word:length of dictionary using dictionary comprehension
words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words}
print("Dictionary of words and their lengths:", word_lengths)
