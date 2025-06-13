# An Ugly Number is a positive number whose prime factors only include 2, 3, and 5.

# ✅ Examples of Ugly Numbers:
# 1 (by definition, considered an ugly number)

# 2, 3, 4, 5, 6, 8, 10, 12, 15, 16, 18, 20, 24, 25...
# An ugly number is defined as a number whose only prime factors are 2, 3, or 5. 
# This means that if the number can be divided by any other prime number, it is not considered an ugly number. 
# Examples of ugly numbers include 1, 2, 3, 4, 5, 6, 8, 9, and 10. Non-examples are 7, 11, 14, and so on.

def is_ugly(n):
    if n <= 0:
        return False
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    return n == 1
print(is_ugly(6))   # 
print(is_ugly(8))   