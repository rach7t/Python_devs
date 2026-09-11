#count character frequency in a string using dictionary
string = "hello world"
def count_char_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    print(frequency)