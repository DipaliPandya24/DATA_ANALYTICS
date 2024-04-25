# Encapsulation
"""
Encapsulation : which wrap data in single entity
which protect data from outside the class
getter and setter method
getter method for get data and setter method for set data
"""
class Student:
    def setId(self,Id):
        self.Id = Id

    def getId(self):
        return self.Id
    
    def setName(self,name):
        self.Name = name
    
    def getName(self):
        return self.Name
    
obj = Student()
# set data
Id = int(input("Enter Id: "))
obj.setId(Id)

# get id using getter method
print(obj.getId())

# set name using setter method
Name = input("Enter name: ")
obj.setName(Name)

# get data
print(obj.getName())

# product name class
class Product:
    # constructor
    def __init__(self):
        self.__mobile = 15000
        self.laptop = 25000
    
    # display method
    def display(self):
         print("Mobile: ",self.__mobile)
         print("Laptop: ",self.laptop)

     # data changing using method
    def changeData(self,mobilenewprice):
        self.__mobile = mobilenewprice


# object
obj = Product()
obj.display()

# change mobile and laptop price
obj.__mobile = 10000
obj.laptop = 35000

obj.display()

print("Change data using method")
# changing moblice price using method
obj.changeData(19000)
obj.display()   