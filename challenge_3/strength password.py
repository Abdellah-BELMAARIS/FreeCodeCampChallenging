def check_strength(password):
    rules = 0
    if len(password) >= 8:
        rules = rules + 1

    has_upper = False
    has_lower = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
    if has_upper and has_lower:
        rules = rules + 1

    has_number = False
    for ch in password:
        if ch.isdigit():
            has_number = True
    if has_number:
        rules = rules + 1

    specials = "!@#$%^&*"
    has_special = False
    for ch in password:
        if ch in specials:
            has_special = True
    if has_special:
        rules = rules + 1

    if rules < 2:
        return "weak"
    elif rules < 4:
        return "medium"
    else:
        return "strong"

print(check_strength("123456"))
print(check_strength("pass!!!"))
print(check_strength("Qwerty"))
print(check_strength("PASSWORD"))
print(check_strength("PASSWORD!"))
print(check_strength("PassWord%^!"))
print(check_strength("qwerty12345"))
print(check_strength("S3cur3P@ssw0rd"))
print(check_strength("C0d3&Fun!"))
