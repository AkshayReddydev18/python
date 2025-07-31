n = int(input("Enter a Number: "))
list = []
for a in range(2,n+1):
    for b in range(2,a):
        if a % b == 0:
            break
    else:
        list.append(a)
print(f'Prime numbers in range of 1 to n are: {list}')