def sock_pairs(pairs, cycles):
    total_socks = pairs * 2

    for cycle in range(1, cycles + 1):
        if cycle % 2 == 0:
            total_socks = max(0, total_socks - 1)

        if cycle % 3 == 0:
            total_socks += 1

        if cycle % 5 == 0:
            total_socks = max(0, total_socks - 1)

        if cycle % 10 == 0:
            total_socks += 2

    return total_socks // 2

print(sock_pairs(2, 5))
print(sock_pairs(1, 2))
print(sock_pairs(5, 11))
print(sock_pairs(6, 25))
print(sock_pairs(1, 8))