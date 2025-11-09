def to_decimal(binary):
    decimal = 0
    power = 0

    for digit in reversed(binary):
        decimal += int(digit) * (2 ** power)
        power += 1

    return decimal
