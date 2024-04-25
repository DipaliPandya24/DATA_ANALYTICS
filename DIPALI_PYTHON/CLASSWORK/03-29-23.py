#  Que. Find even odd number+

#  accept number from user
n = int(input("Enter number: "))

#  check condition
if num%2==o:
    #output
    print("even number")
else:
    print("odd number")

# user defined exception example
#  Create class which inherite exception

# user defined exception
class OddException(Exception):
    pass

# ---------------------------------------------------------------------------
# main program executation
#  accept number from user
n = int(input("Enter number: "))

try:
    # check condition
    if n%2==0:
        print("Even numbers")
    else:
        # raise exception
        raise OddException
except OddException:
    print("We can't accept odd numbers")


# ADVANCED PYTHON STARTED.......................................
"""
OOPS: object oriented programming system

class : class is a collection data type which contain data number and number function is a single entity
    syntax:

problem

def addstudent:
    pass
    
def addfaculty:
    pass
    
def viewstudent:
    pass
"""

# class creation
class Student:
    # data memers in class variable
    name = "deepak"
    subject = "python"
    technology = "programming"

    #  member function in class
    # self : which is represent current class properties
    def display(self):
        print("name = ", self.name)
        print("subject = ", self.subject)

# object creation
obj = Student()
obj.display()

# # class creation
class Faculty:
    # data memers in class variable
    name = "anjali"
    subject = "python"
    ct = "DA"

    #  member function in class
    # self : which is represent current class properties
    def display(self):
        print("name = ", self.name)
        print("subject = ", self.subject)

# object creation
obj = Faculty()
obj.display()

"""
We can create, read and write file using python
There are 4 modules in pythin file handling
r : read
w : write
x : create
a : append mode
"""
# # take one variable which open file
f = open("myfile.txt", "r")
print (f.read())

# # take one variable which open file
with open("myfile.txt", "r") as f:
    print (f.read())

# # open any file in specific variable
f = open("mynew_file.txt", "w")
#  accept number from user
name = input("enter name : ")
#  using of write() write file
f.write("\n",name)
# close file
f.close()

# open any file in specific variable
f = open("mynew_file.txt", "a")
#  accept number from user
name = input("enter name : ")
#  using of write() write file
f.write("\n"+name)
# close file
f.close()

#  create blank file
f = open("blankfile.txt", "x")
f.close()