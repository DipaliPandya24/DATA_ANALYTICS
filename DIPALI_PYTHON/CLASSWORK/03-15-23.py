"""
Function: Function is a block of code that code are used to again and again.
Using of function we can reduce our code. Fuunction provide reusabilities.
In python: there are 2 steps to implement,
1) function defination      2) function calling
Function defination:
        syntax:
    def <funname>():
        statement

        
def myfun():
    print("Hello")
    print("Welcome to Python")

myfun()
myfun()
myfun()

def greetings():
    msg = input("Enter your msg : ")
    print(msg)

greetings()
greetings()


def add():
    num1 = int(input("Enter num 1 : "))
    num2 = int(input("Enter num 2 :"))
    ans = num1 + num2
    print(ans)

def mul():
    num1 = int(input("Enter num 1 : "))
    num2 = int(input("Enter num 2 :"))
    ans = num1 * num2
    print(ans)

def menu():
    data = """"""
                        Menu

                    Press 1 for addition
                    Press 2 for multiplication
            """"""
    print(data)
    choice = int(input("Enter your choice: "))
    if choice ==1:
        add()
    elif choice ==2:
        mul()


menu()

Function catageries
There are 4 types of catagories
1) function without parameters and function without return types
2) function with parameters and function without return types
3) function without parameters and function with return types
4) function with parameters and function with return types
"""

#WAP which accept value from user and check entered number is even or odd and entered number is positive or negative

def even_odd():    
    n = int(input("Enter number: "))
    if n%2==0:
        print("It is even")
    else:
        print ("It is odd")
def neg_pov():
    n = int(input("Enter number: "))
    if n>0:
        print("It is positive")
    else:
        print ("It is negative")

even_odd()
neg_pov()

#function with parameters and function without return types (type2)
def myfun(num1,num2):
    print(num1)
    print(num2)

myfun(10,20)

def swap(num1,num2):
    print(num1)
    print(num2)
    num1,num2 = num2,num1
    print(num1)
    print(num2)

swap(100,200)