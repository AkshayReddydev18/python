n = int(input("Enter a number :"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(n):
        if j ==0 or i==0 or i==n-1 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    