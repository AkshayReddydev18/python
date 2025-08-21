'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]

Enter list:[10,20,15,12,5]
[5, 10, 12, 15, 20]
'''

a = eval(input("Enter the to be sorted list:")) # [10,20,30,25,40,35,12,5]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)
