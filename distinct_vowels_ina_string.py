'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes

Enter String:RamA raO
{'A': 3, 'O': 1}
'''

x1 = input("Enter a string:")
b = {}
x1 = sorted(x1.upper())
x2 = set('AEIOU')
for x in x1:
    if x in x2:
        b[x] = b.get(x,0)+1
print(b)


