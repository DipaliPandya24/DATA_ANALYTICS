"""
programme 1
n= int(input(" Enter the value= "))
if n>0:
    print("It is positive")
else:
    print("It is negative")


programme 2
n= int(input(" Enter the value= "))
if (n%2)==0:
    print("It is even")
else:
    print ("It is odd")

programme 3
n1= int(input(" Enter the value= "))
n2= int(input(" Enter the value= "))
if(n1>n2):
    print("N1 is maximum")
else:
    print("N2 is maximum")

programme 4
n1= int(input("Enter A= "))
n2= int(input("Enter B= "))
n3= int(input("Enter C= "))

print("A=",n1,"B=",n2,"C=",n3)

if n1>n2:
    if n1>n3:
        print(n1,"is greater")
    else:
        print(n3,"is greater")
else:
    if n2>n3:
        print(n2,"is greater")
    else:
        print(n3,"is greater")
"""
#WAP to get student's percentage using ladder if else
roll= int(input("Enter your Roll No.: "))
name= input("Enter your name: ")
p= int(input("Enter Physics marks"))
m= int(input("Enter Maths marks"))
c= int(input("Enter Chemistry marks"))
total= (p+m+c)
per= (total/3)
print()
print("Roll no.: ",roll)
print("Name: ",name)
print("Total: ",total)
print("Percentage: ",per)


if per>=75:
      print("Class is Distinction")
elif per>=65:
        print("First Class")
elif per>=55:
        print("Second Class")
elif per>=45:
        print("Pass Class")
else:
        print("Fail")













