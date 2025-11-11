import math

def goldilocks_zone(mass):
    luminosity = mass ** 3.5

    sqrt_luminosity = math.sqrt(luminosity)

    start = 0.95 * sqrt_luminosity
    end = 1.37 * sqrt_luminosity

    return [round(start, 2), round(end, 2)]

print(goldilocks_zone(1))
print(goldilocks_zone(0.5))
print(goldilocks_zone(6))
print(goldilocks_zone(3.7))
print(goldilocks_zone(20))