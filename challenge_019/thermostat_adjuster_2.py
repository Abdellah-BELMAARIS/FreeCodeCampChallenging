def adjust_thermostat(current_f, target_c):
    target_f = (target_c * 1.8) + 32

    if current_f < target_f:
        difference = round(target_f - current_f, 1)
        return f"Heat: {difference} degrees Fahrenheit"

    elif current_f > target_f:
        difference = round(current_f - target_f, 1)
        return f"Cool: {difference} degrees Fahrenheit"

    else:
        return "Hold"

print(adjust_thermostat(32, 0))
print(adjust_thermostat(70, 25))
print(adjust_thermostat(72, 18))
print(adjust_thermostat(212, 100))
print(adjust_thermostat(59, 22))