
x = int(input("Enter 1st Number: "))
y = int(input("Enter 2nd Number: "))
z = int(input("Enter 3rd Number: "))
list=[]
n = min(x,y,x)
for i in range(1,n+1):
    if(x%i==0 and y%i==0 and z%i==0):
        list.append(i)
print(f'GCD of {x,y,z} is {list[-1]}')
        

# import math

# x = int(input("Enter 1st Number: "))
# y = int(input("Enter 2nd Number: "))
# z = int(input("Enter 3rd Number: "))

# x = math.gcd(x,y,z)
# print(x)
    
   