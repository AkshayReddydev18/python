def is_palindrome(s):
    s = s.lower().replace(" ", "")  # ignore case and spaces
    return s == s[::-1]

# Example usage
word = "Madam"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
