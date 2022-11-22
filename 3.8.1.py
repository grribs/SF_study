test_matrix = [
    [1, 2, 3],
    [7, -1, 2],
    [123, 2, -1]
]

max_element = int(0)

for row in test_matrix:
    for element in row:
        if element > max_element:
            max_element = element
print(max_element)
