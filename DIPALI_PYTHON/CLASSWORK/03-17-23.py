"""
Function categories:
There are 4 types of function categories
1) Funtion without parameter and without return type
        syntax: def <funname>()
            //block of code
            
        <funname>()

2) Function with parameter and without return type
              syntax:   def add(n1,n2):
                            //operation

                        def mul(n1,n2):
                            //operation  

3) Function with parameter and with return type    
4) Function without parameter and with return type 

db = dict
"""
db = {} #blank dict
def registration(firstname,email,password):
    db['name'] = firstname
    db['email'] = email
    db['password'] = password
    print("Registration Successfull !!!!")

def login(email,password):
    if email == db['email']:
        if password == db['password']:
            return db['name']
        else:
            return "Invalid email or password"
    else:
            return "Invalid email or password"
status = True
while status:

    menu = """
            1) press 1 for registration
            2) press 2 for login
            3) press 3 for exit
        """
    print(menu)

    choice = int(input("Enter your choice"))
    if choice == 1:
     name = input("Enter name: ")
     email = input("Enter email: ")
     password = input("Enter password: ")

     registration(name,email,password)
     
    elif choice == 2:
        email = input("Enter email: ")
        password = input("Enter password: ")
        print(login(email,password))

    elif choice == 3:
        status = False

"""
*args: arguments (tuple as parameter)
*kwrgs: key with arguments (dict as a parameter)
"""
# normal function with normal parameter

def sum(n1,n2):
    ans = n1 + n2
    print(ans)
sum(10,20)

# args function

def addition(*n):
    ans = 0
    for i in n:
        ans += i
    print(ans)

addition(10,20,30,40,50,60,70,80,90)

# kwrgs

def myfun(**kwrgs):
    for k,v in kwrgs.items():
        print(f"{k} = {v}")

myfun(name="Dipali", subject="Python")