"""
import random
computer = random.randint(1,100)
status = True
while status:
    user = int(input("Enter a number: "))
    if user>computer:
        print("Hint: guess a lower number: ")
    elif user<computer:
        print("Hint: guess a higher number: ")
    else:
        print("You won!!!")

#WAP accept 5 numbers from user and store it in existing list
n1 = int(input("Enter a number N1: "))
print (" Number is: ",n1)
n2 = int(input("Enter a number N2: "))
print (" Number is: ",n2)
n3 = int(input("Enter a number N3: "))
print (" Number is: ",n3)
n4 = int(input("Enter a number N4: "))
print (" Number is: ",n4)
n5 = int(input("Enter a number N5: "))
print (" Number is: ",n5)

l= [n1,n2,n3,n4,n5]
print(l)

#WAP accept 5 numbers from user and store it in existing list
l1 = []
for i in range(1,6):
    if num = int(input("Enter a number: ")):
        print (" Number is: ")
l1.append[num]

 #find unique values or remove duplicate values
l1= [23,67,23,7,9,7]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)

List is a collection data type which is contain similar and dis-similsr data
elements at a single location, list is mutable (changeable), list is orderable,
list is a indexable 

l1 = [12,23,54,67,89,54,3]
print(l1[2])
print(l1[2:6])
print(l1[-1])
print(l1[-3:-1])
print(l1[-3:])
print(l1[-2:])

#Nested List
l1 = [10,20,[101,102,103,[201,202,203]]]

print(l1[1])
print(l1[2][0])
print(l1[2][3][0])

Set: Set is a collection data type which contain only unique values set
is unorderable, set is unindexable, set is immutable
Syntax:
    set = {}
"""
#find unique values or remove duplicate values
s= {12,23,45,2,12,5,6,23}
print(s)



















    
