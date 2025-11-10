def to_binary(decimal):
    decimal = int(decimal)
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary


print(to_binary(5))
print(to_binary(12))
print(to_binary(50))
print(to_binary(99))
