"""
TASK: Accept number from user raise exception if user enter below zero value
"""
# # user defined exception
class NegativeNumbers(Exception):
    pass

# ---------------------------------------------------------------------------
# main program executation
#  accept number from user
n = int(input("Enter number: "))

try:
    # check condition
    if n>0:
        print("Postive number")
    else:
        # raise exception
        raise NegativeNumbers
    
#it will execute when user enter below zero
except NegativeNumbers:
    print("We can't accept negative numbers")

"""
TASK: Accept number from user raise exception when first number is smaller than second
"""
# user defined exception
class GreaterNum(Exception):    
    pass
# Accept numbers from user
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

try:
    # check condition
    if n1<n2:
        print("n2 is greater")
    else:
        # raise exception
        raise GreaterNum

#it will execute when user entere n1>n2
except GreaterNum:
    print("n1 should not be greater than n2")