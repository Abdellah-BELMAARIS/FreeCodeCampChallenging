def to_12(time):
    hours = int(time[:2])
    minutes = time[2:]

    if hours == 0:
        return f"12:{minutes} AM"
    elif hours < 12:
        return f"{hours}:{minutes} AM"
    elif hours == 12:
        return f"12:{minutes} PM"
    else:
        return f"{hours - 12}:{minutes} PM"

print(to_12("1124"))
print(to_12("0900"))
print(to_12("1455"))
print(to_12("2346"))
print(to_12("0030"))