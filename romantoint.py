x = input("Enetr a Roman Number:")
roman_values = {
    'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
    }
total_value = 0
prev_value = 0
# for char in x:
#     current_value = roman_values[char]
#     if current_value > prev_value:
#         total_value += current_value - 2 * prev_value
#         # prev_value = current_value
        
#     else:
#         total_value += current_value 
#     prev_value = current_value
# print(total_value)


for char in reversed(x):
    current_value = roman_values[char]
    if current_value < prev_value:
        total_value -= current_value
    else:
        total_value += current_value
    prev_value = current_value
print(total_value) 