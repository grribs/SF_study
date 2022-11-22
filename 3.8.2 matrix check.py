test_matrix = [
    [1, 2, 3],
    [7, -1, 2],
    [123, 2, -1]
]

num_lines = len(test_matrix)
row = []
a = True

for row in test_matrix:
    if len(row) == num_lines:
        a = True
    else:
        a = False

print(a)

'''

#print(num_lines)


#col_test = []





'''