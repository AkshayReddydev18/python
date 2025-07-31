n =int(input("Enter a nth Term of fibonacci Series: "))
a,b = 0,1
list = [0,1]
c = a+b
while c <= n:
    list.append(c)
    a=b
    b=c
    c= a+b
print(list)



# n = int(input("Enter a nth Term of Fibonacci Series: "))
# a, b = 0, 1
# fib_list = [a]

# while b <= n:
#     fib_list.append(b)
#     a, b = b, a + b

# print(f'Fibonacci Series up to{n} is:{ fib_list}')

