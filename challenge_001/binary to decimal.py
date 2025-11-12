def to_decimal(binary):
    decimal = 0
    power = 0
    for digit in binary[::-1]:
        if digit == '1':
            decimal += 2 ** power
        power += 1

    return decimal

print(to_decimal("101"))
print(to_decimal("1010"))
print(to_decimal("10010"))
print(to_decimal("1010101"))
