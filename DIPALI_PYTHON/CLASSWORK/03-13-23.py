"""
list and tuple :
both are collection of data type

list: list is a mutale data type which contain data number in single location
    list is represented by []
    list which is indexable, orderable and muteable(changeable)

tuple: tuple is a collection of data type,
    tuple is indexable, orderable
    tuple is immutable
    tuple is represented by ()
"""

t = (10,20,30)
print(type(t))
print(t)

t = ("Python")
print(type(t))

t = ("Python",)
print(type(t))

t = ("Python","Java","Android","Flutter","React")
print(t)

for item in t:
    print(item)

t = ("Python","Java","Android","Flutter","React")
print(t)

for item in t:
    print(item,end=" ")

t = ("Python","Java","Android","Flutter","React")
print(t)
print(len(t))


t = ("Pyton","Java","C","Java","Php")
print(t.count("Java"))

t = ("Pyton","Java","C","Java","Php")
l1 = list(t)    # casting into list
l1[0] = "Flutter"
t = tuple(l1)   # recasting into tuple
print(t)



"""
import random

n = random.randint(1,100)
print(n)

l1 = ["Python","Java","Android","Php"]
print(random.choice(l1))

"""