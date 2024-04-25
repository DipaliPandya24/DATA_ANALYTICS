
# 1. What is file function in python
# Ans. Python file object provides methods and attributes to access and manipulate files. Using file objects, we can read or write any 
# files. Whenever we open a file to perform any operations on it, Python returns a  file objectPython file object provides 
# methods and attributes to access and manipulate files. Using file objects, we can read or write any files. Whenever we open a file to 
# perform any operations on it, Python returns a file object.

# Write a Python program to read an entire text file.
# take one variable which open file
f = open("myfile.txt", "r")
print (f.read())

# Write a Python program to append text to a file and display the text
# open any file in specific variable
f = open("mynew_file.txt", "a")
#  accept number from user
name = input("enter name : ")
#  using of write() write file
f.write("\n"+name)
# close file
f.close()

# Write a Python program to read first n lines of a file.
#  accept number from user
n = int(input("Enter number of lines to read: "))
# take one variable which open file
f = open("myfile.txt", "r")
for i in range(n):  # check condition
	print(f.readline()) #output


# Write a Python program to read last n lines of a file.
n = int(input("Enter number of lines to read: "))
# take one variable which open file
f = open("myfile.txt", "r")
for i in range(n):  # check condition
	print(f.readline()) #output
