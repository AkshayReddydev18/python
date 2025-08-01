# import inflect

# n = int(input("Enter a Number: "))
# p = inflect.engine()
# words = p.number_to_words(n)
# print(words)


import inflect

n = int(input("Enter a Number: "))

def number_to_words(n):
    p = inflect.engine()
    return p.number_to_words(n)
print(number_to_words(n))