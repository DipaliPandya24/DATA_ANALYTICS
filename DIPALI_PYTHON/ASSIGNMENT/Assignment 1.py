"""
MODULE 1 - PYTHON ASSIGNMENT

#1. WAP sum of first n +ve integers
n = int(input("Enter the No.:"))
sum=0
for i in range(0,n+1):
    sum=sum+i
    n=n-1


print("Sum:",sum)

#2. WAP to count occurrences of a substring in a string
s = "Hello Python Programming"
print(s)
print(s.count("o"))


#3. WAP to count occurrence of each woprd in a given sentence
s = "It's not okay to be okay"
r = input("Enter the word: ")
a=[]
count=0
a = s.split(" ")
for i in range(0,10):
    if(r==a[i]):
        count = count+1
print("Count of word is: ", count)


#4. WAP to get a single string from two given string, seperate by a space and swap the first two characters of each string.
s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")
print(s1)
print(s2)

s1,s2=s2,s1
print("After swapping String 1=", s1, "String 2=", s2)


#5. WAP to add 'ing' at the end of a given string (length should be at least 3).If the given string already ends with 'ing' then add 'ly' instead If the string length of the given string is less than 3, leave it unchanged
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == "ing":
      str1 += "ly"
    else:
      str1 += "ing"

  return str1
print(add_string("dp"))
print(add_string("dpp"))
print(add_string("string"))


#6. WAP to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
#Return the resulting string
def not_poor(s1):
  snot = s1.find('not')
  spoor = s1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    s1 = s1.replace(s1[snot:(spoor+4)], 'good')
    return s1
  else:
    return s1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))

#7. WAP to find the greatest common divisor of two numbers
from math import gcd


a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))
gcd(a,b)
print("The gcd of number1 and number2 is: ", gcd(a,b))


#8. WAP to check whether a list contains a sublist
l1 = [0,1,2,3,4,5,6,7,8,9]
l2 = [2,4,6,18]
print(l1)
print(l2)
if (set(l2).issubset  (set(l1))):
    print("L2 is subset of L1")
else:
    print("L2 is not the subset of L1")

#9. WAP to find the second smallest number in a list
l1 = [100,101,102,103,104,105]
l1.sort()
print("Second smallest number: ", l1[1])

#10. WAP to get unique values from a list
s = {10,20,30,30,20,10,61,35,61,35}
print(s)

#11. WAP to unzip of tuples into individual lists.
t = (10,20,30,40,50,60)
print(t)

for item in t:
    print(item)
#12. WAP to convert of tuples into dictionary.
t = [("One", 1), ("Two", 2)]
print(t)
my_dict = dict(t)
print(my_dict)

#13. WAP to sort a dictionary (ascending/descending)by value
my_dict = {"Dipali":16, "Khushi":6, "Heny": 22}
mykeys = list(my_dict.keys())
for i in mykeys:
    mykeys.sort
sorted_dict = {i: my_dict[i]}
print(sorted_dict)

#14. WAP to find the highest 3 values in a dictionary
from collections import Counter


my_dict = {'t': 3, 'u': 4, 't': 6, 'o': 5, 'r': 21}
k = Counter(my_dict)
# Finding 3 highest values
high = k.most_common(3)
print("Dictionary with 3 highest values:")
print("Keys: Values")
for i in high:
   print(i[0]," :",i[1]," ")

#15. Give a number n, write a python program to make and print the list of
# Fibonacci numbers upto n.
n = int(input("Enter the number of fibbonacci : "))
f = 0 
s = 1

print(f)
print(s)

for i in range(3,n+1):
    t = f + s
    print(t)
    f = s 
    s = t 

#16. Counting the frequencies in a list using a dictionary in Python.
l1 = [1,2,3,1,2,6,1,3,5,2,3,4,1,3,9]
freq = {}
for item in l1:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1
 
for key, value in freq.items():
    print ("% d : % d"%(key, value))

#17. WAP using function to find the sum of odd series and even series

#18. WAP to Find Factorial of Number Using Recursion
def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return (n * factorial(n-1))
num = int(input("Enter the number: "))
print("Number: ", num)
print("Factorial: ", factorial(num))

#19. WAP that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,1,2,2,3,3,3,3,4,5])) 

#20. Make a program to generate a strong password using the input given by the user. To generate a password,
#randomly take some words from the user input and then include numbers, special characters and capital
#letters to generate the password. Also, keep a check that password length is more than 8 characters.

import array
import random


MAX_LEN = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


for x in range(MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)

	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
		password = password + x
		
print(password)
"""