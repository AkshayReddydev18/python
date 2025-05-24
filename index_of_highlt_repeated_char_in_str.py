# print the indexes of the most highly repeated character in a string

def most_repeated_index_of_char(input):
    max_count = 0
    max_char = ""
    for  i in input:
        count = input.count(i)
        if count > max_count:
            max_count = count
            max_char = i 
    # print(f"indexes of '{max_char}':")
    for i in range(len(input)):
        if input[i] == max_char:
            print(i, end=" ")
        
   
input="MISSISSIP"
input = "banana"

most_repeated_index_of_char(input)
print()                  
            
        
        