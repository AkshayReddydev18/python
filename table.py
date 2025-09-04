for j in range(1,11):
    for i in range(6,16):
        if   (len(str(i*j)) == 3 and j == 10):
            print(f' {i} x{j} ={i*j} ',end ='|')
        elif (len(str(i*j)) == 2 and j == 10):
            print(f' {i} x{j} = {i*j} ',end ='|')
        elif len(str(i*j)) ==3 :
            print(f' {i} x {j} ={i*j} ',end ='|')
        elif len(str(i*j)) == 2 :
            print(f' {i} x {j} = {i*j} ',end ='|')
        elif len(str(i*j)) == 1:
            print(f' {i} x {j} =  {i*j} ',end ='|')
        else:
            print(f' {i} x {j} = {i*j} ',end ='|')
    print()
print('-'*136)