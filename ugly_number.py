# An Ugly Number is a positive number whose prime factors only include 2, 3, and 5.

# ✅ Examples of Ugly Numbers:
# 1 (by definition, considered an ugly number)

# 2, 3, 4, 5, 6, 8, 10, 12, 15, 16, 18, 20, 24, 25...

def is_ugly(n):
    if n <= 0:
        return False
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    return n == 1
print(is_ugly(6))   # 
print(is_ugly(8))   