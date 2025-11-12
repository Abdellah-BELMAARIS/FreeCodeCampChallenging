def format(seconds):

    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    seconds_str = f"{seconds:02d}"

    if hours > 0:
        return f"{hours}:{minutes:02d}:{seconds_str}"
    else:
        return f"{minutes}:{seconds_str}"

print(format(500))
print(format(4000))
print(format(1))
print(format(5555))
print(format(99999))