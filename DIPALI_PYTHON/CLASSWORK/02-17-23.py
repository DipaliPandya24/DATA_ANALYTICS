"""
TYPE 1 WHILE LOOP


Programme 1
n= int(input("Enter the no.= "))
while n>0:
    print("Tops Tech")
    n=n-1

Programme 2
#WAP to print 1 to 20
n = 1
while n<=20:
    print(n)
    n= n+1

Programme 3
#WAP to print the sum of nos.
n = int(input("Enter the no.= "))
sum=0
while n>0:
    sum = sum+n
    n = n-1
    
print("Sum=",sum)




TYPE 2 FOR LOOP

#1st variant
for i in range(10):
    print(i)


#2nd variant
for i in range(1,10):
    print(i)


#3rd variant
for i in range(5,50,8):
    print(i)

#4th variant
for i in range(20,0,-1):
    print(i)
"""
#WAP to write the sum of integers
n = int(input("Enter No.:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    n=n-1

print("Sum:",sum)



















