#wap to get the frequency of each character in a string
string = "Python Programming"
emergency = {}
for char in string:
    emergency[char] = emergency.get(char, 0) + 1
print("Character frequencies:")
for char, freq in emergency.items():
    print(f"'{char}': {freq}")



#wap to print even and odd positions of a  character in a string
string = "Python Programming"
print("Characters at even positions:")
for i in range(0, len(string), 2):
    print(f"Position {i}: '{string[i]}'")
print("Characters at odd positions:")
for i in range(1, len(string), 2):
    print(f"Position {i}: '{string[i]}'")



#wap to remove duplicate characters from a string
string = "Python Programming"
unique_chars = []
for char in string:
    if char not in unique_chars:
        unique_chars.append(char)
result = ''.join(unique_chars)
print(f"String after removing duplicates: {result}")



#wap to print first not repeated character in a string
string = "Python Programming"
emergency = {}
for char in string:
    emergency[char] = emergency.get(char, 0) + 1
for char in string:
    if emergency[char] == 1:
        print(f"First non-repeated character: '{char}'")
        break
else:
    print("No non-repeated character found.")

#wap to print first repeated character in a string
string = "Python Programming"
emergency = {}
for char in string:
    emergency[char] = emergency.get(char, 0) + 1
for char in string:
    if emergency[char] > 1:
        print(f"First repeated character: '{char}'")
        break
    else:
      print("No repeated character found.")


