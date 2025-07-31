sentence = input("Enter a Sentence: ")
longest_word = ''
current_word = ''
for char in sentence:
    if char == ' ':
        if len(current_word) > len(longest_word):
            longest_word = current_word
        current_word = ''
    else:
        current_word += char
if len(current_word) > len(longest_word):
    longest_word = current_word
print(longest_word)