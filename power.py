
def power(a, b):
    if b == 0:
        return 1
    if b < 0:
        if a == 0:
            raise ValueError("0 cannot be raised to a negative power")
        return 1 / power(a, -b)
    return a * power(a, b - 1)

# a= (input('a:')), 
# b=(input('b:'))#= 4, -1  # a and b can be +ve, -ve, or 0
print(power(4, -1))