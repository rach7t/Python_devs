#program that writes a message in the file ,data.txt
file = open("data.txt",'w')
file.write("Hello all \n")
file.write("Hope you are enjoying")

file.close()
print("Data written into file..")