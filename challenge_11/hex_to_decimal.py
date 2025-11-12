def hex_to_decimal(hex):
    decimal = 0
    hex_digits = "0123456789ABCDEF"

    for i, char in enumerate(reversed(hex)):

        digit_value = hex_digits.index(char.upper())

        decimal += digit_value * (16 ** i)

    return decimal

print(hex_to_decimal("A"))
print(hex_to_decimal("15"))
print(hex_to_decimal("2E"))
print(hex_to_decimal("FF"))
print(hex_to_decimal("A3F"))