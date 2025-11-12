def mask(card):
    digits = [char for char in card if char.isdigit()]

    masked_digits = ['*'] * (len(digits) - 4) + digits[-4:]

    result = []
    digit_index = 0

    for char in card:
        if char.isdigit():
            result.append(masked_digits[digit_index])
            digit_index += 1
        else:
            result.append(char)

    return ''.join(result)

print(mask("4012-8888-8888-1881"))
print(mask("5105 1051 0510 5100"))
print(mask("6011 1111 1111 1117"))
print(mask("2223-0000-4845-0010"))
# print(mask("4545 4124 5874 1220"))