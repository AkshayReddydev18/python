n = int(input("Enter a Number:"))
for i in range(n,0,-1):
    # print(' '*(n-i)+'*'*(2*i-1))
    for j in range(n-i):
        print(" ",end='')
    for k in range(2*i-1):
        print('*',end='')
    print()