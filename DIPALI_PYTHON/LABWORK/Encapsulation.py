class Faculty:
    def setId(self,Id):
        self.Id = Id

    def getId(self):
        return self.Id
    
    def setName(self,name):
        self.Name = name
    
    def getName(self):
        return self.Name
    
    def setTech(self,Tech):
        self.Tech = Tech
    
    def getTech(self):
        return self.Tech
    
obj = Faculty()
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

# set Tech using setter method
Tech = input("Enter Tech: ")
obj.setTech(Tech)

# get data
print(obj.getTech())