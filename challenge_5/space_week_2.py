def has_exoplanet(readings):
    values = []

    for char in readings:
        if char.isdigit():
            values.append(int(char))
        else:
            values.append(ord(char) - ord('A') + 10)
    avg = sum(values) / len(values)

    for value in values:
        if value <= 0.8 * avg:
            return True

    return False


print(has_exoplanet("665544554"))
print(has_exoplanet("FGFFCFFGG"))
print(has_exoplanet("MONOPLONOMONPLNOMPNOMP"))
print(has_exoplanet("FREECODECAMP"))
print(has_exoplanet("9AB98AB9BC98A"))
print(has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGE"))



