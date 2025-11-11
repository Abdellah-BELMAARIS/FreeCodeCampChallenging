def send_message(route):

    total_distance = sum(route)

    transmission_time = total_distance / 300000

    num_satellites = len(route) - 1

    total_delay = num_satellites * 0.5

    total_time = transmission_time + total_delay

    return round(total_time, 4)


print(send_message([308080, 308080]))
print(send_message([384400, 384400]))
print(send_message([54600000, 54600000]))
print(send_message([1000000, 500000000, 1000000]))
print(send_message([10000, 21339, 50000, 31243, 10000]))
print(send_message([802101, 725994, 112808, 3625770, 481239]))

