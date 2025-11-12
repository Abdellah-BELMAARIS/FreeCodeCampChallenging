def dive(map, coordinates):
    row, col = coordinates
    current_value = map[row][col]

    if current_value == "-":
        return "Empty"
    elif current_value == "O":
        map[row][col] = "X"
        for r in range(len(map)):
            for c in range(len(map[0])):
                if map[r][c] == "O":
                    return "Found"
        return "Recovered"
    elif current_value == "X":
        for r in range(len(map)):
            for c in range(len(map[0])):
                if map[r][c] == "O":
                    return "Found"
        return "Recovered"

print(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]))
print(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]))
print(dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]))
print(dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]))
print(dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]))
print(dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]))