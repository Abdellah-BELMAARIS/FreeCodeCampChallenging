def count(text, parameter):
    count = 0

    for i in range(len(text) - len(parameter) + 1):
        if text[i:i+len(parameter)] == parameter:
            count += 1

    return count

print(count('abcdefg', 'def'))
print(count('hello', 'world'))
print(count('mississippi', 'iss'))
print(count('she sells seashells by the seashore', 'sh'))
print(count('101010101010101010101', '101'))
