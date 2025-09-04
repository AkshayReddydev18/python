list = eval(input("Enter a list:"))
# [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
# mod = ''
# ctr = 0
# for x in list:
#     if list.count(x) > ctr:
#         mod = x
#         ctr = list.count(x)
# print(mod)



# print('mode: ',max(list,key = list.count))


dict = {}
for x in list:
    dict[x] = dict.get(x, 0) + 1

max_count = max(dict.values())

mode = [k for k,v in dict.items() if v == max_count]

print(f'mode is : {mode}' if len(mode) == 1 else f'modes are: {mode}')