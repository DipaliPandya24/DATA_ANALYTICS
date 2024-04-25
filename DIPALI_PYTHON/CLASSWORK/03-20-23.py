"""
Lambda function:
    Function without any name is called lambda function.
    Lambda function is a anonymous function
    syntax
    var lambda args : expression

# normal function

def sum(n1,n2):
    ans = n1 + n2
    return ans

print(sum(12,23))

# Lambda funtion

ans = lambda num1, num2 : num1 + num2
print(ans(12,23))


Filter
filter() : filter is a method which filters given sequence with the help of function that test's each element of the sequence.
    syntax:
        filter(fun, sequence)

# checking vowel in list without filter

l1 = ['a', 'e', 'v', 'j', 'a']

vowels_list = ['a', 'e','i', 'o', 'u']

l2 = []

def checkVowel():
    for c in l1:
        if c in vowels_list:
            l2.append(c)

checkVowel()
print(l2)

for i in l2:
    print(i)

# checking vowel in list with filter

l1 = ['a', 'e', 'v', 'j', 'a']

vowels_list = ['a', 'e','i', 'o', 'u']

def myfun(seq):
    if (seq in vowels_list):
        return True
    else:
        return False
    
filtered_data = filter(myfun, l1)

for i in filtered_data:
    print(i)



data_set = [12,23,45,6,4,78,5,3,33,67]

def myfun(data): # type: ignore
    if data %2 ==0:
        return True
    else:
        return False

filtered_data = filter(myfun, data_set)
for i in filtered_data:
    print(i)


# filtered subject available in existing list or not
subject = ["English", "Maths", "Java", "Android",]
tops_subject = ["c", "c++", "Java", "Android", "Flutter"]

def myfun(seq):
    if (seq in tops_subject):
        return True
    else:
        return False
    
filtered_data = filter(myfun,subject)

for i in filtered_data:
    print(i)       
"""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               