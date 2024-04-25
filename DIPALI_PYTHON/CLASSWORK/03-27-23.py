"""
Exception : which disturb the normal flow of the program
        exception which is handle by try and except block

        its called exception handling.
exception handling syntax:

        try:
                exception code
        except:
                statement
        
"""
# without exception handling code
print(a)

# with exception handling code
try:
       print(a) 
except:
       print("Variable declaration not done")

try:
        # Accept numbers from user
        n1 = int(input("Enter number 1: "))
        n2 = int(input("Enter number 2: "))

        # calculation
        ans = n1/n2
        #  display output
        print(ans)
except:
        print("Invalid output")

try:
        # Accept numbers from user
        n1 = int(input("Enter number 1: "))
        n2 = int(input("Enter number 2: "))

        # calculation
        ans = n1/n2
        #  display output
        print(ans)
except ValueError:
        print("Invalid output only 0-9 required")
except ZeroDivisionError:
        print("Cannot be divided by zero")
except:
        print("Invalid output")

"""
try:
        exception block
except:
        after exception executable statement
else:
        without exception
finally:
        it always occur
"""

try:
    #variable defination
    a = 10
    b = "a"
    ans = a + b
    print(ans)

except:
    print("Invalid input")

else:
    print("Welcome to math world")
#  It always excute exception occur or not
finally:
    print("THANK YOU FOR USING THIS APP.")

# list define
l1 = [10,20,30,40,50]

# display list
print(l1)

try:
    #access specific element from the list
    print(l1[9])
except:
    print("list index out of bound")
else:
    #display list
    print(l1)

try:
    print(a)
except Exception as e:
    print(e)

# import sys module
import sys
# exception handling block
try:
    print(a)
except:
    print("Subject = ", sys.exc_info()[0])
    print("message = ", sys.exc_info()[1])