def launch_fuel(payload):
    mass = float(payload)
    fuel = 0.0

    while True:
        fuel_needed = mass / 5.0
        additional = fuel_needed - fuel

        fuel = fuel_needed

        if additional < 1.0:
            break
        mass = payload + fuel

    return round(fuel, 1)


print(launch_fuel(50))
print(launch_fuel(500))
print(launch_fuel(243))
print(launch_fuel(11000))
print(launch_fuel(6214))
