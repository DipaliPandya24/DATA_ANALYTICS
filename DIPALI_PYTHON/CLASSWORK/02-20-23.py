"""
#Programme 1
n=int(input("Enter number "))
evensum=0
oddsum=0

for i in range(1,n+1):
      #print(i)
      if i%2==0:
          print("Even : ",i)
          evensum = evensum+i
      else:
          print("Odd : ",i)
          oddsum = oddsum+i

#break: It is used to stop the loop
#pattern 1
for i in range(1,10):
    print("*"*(9-i))

#pattern 2
for i in range(1,10):
    print("*"*i)

#pattern 3
for i in range(1,11):
    print(" "*(10-i), "*"*i)

#pattern 4
for i in range (1,11):
    print(" "*(10-i)," *"*i)

#pattern 5
for i in range (1,11):
    print(" "*(10-i)," *"*i)
for i in range(10,0,-1):
    print(" "*(10-i)," *"*i)

#b1
for i in range(1,10):
    if i==5:
        break
    else:
        print("I:",i)  
  
#break: It is used to break the loop
#b2
for i in range(1,10):
    if i==5 and i==7:
        break
    else:
        print("I:",i)


#b3
for i in range(1,10):
    if i==5 or i==7:
        break
    else:
        print("I:",i)

#continue: It is used to skip the condition

#c1
for i in range(1,10):
    if i%2==0:
        continue
    else:
        print(i)

#c2
for i in range(1,10):
    if i==4 or i==7:
        continue
    else:
        print("I:",i)
"""










