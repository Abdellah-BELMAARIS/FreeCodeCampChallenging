def find_landing_spot(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    safest_spot = None
    min_danger = float('inf')

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                danger_sum = 0

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy

                    if 0 <= ni < rows and 0 <= nj < cols:
                        danger_sum += matrix[ni][nj]

                if danger_sum < min_danger:
                    min_danger = danger_sum
                    safest_spot = [i, j]

    return safest_spot

print(find_landing_spot([[1, 0], [2, 0]]))
print(find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]))
print(find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]))
print(find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]))