import random

def generate_random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def get_column_sum(matrix, col_index):
    column_sum = 0
    for row in matrix:
        column_sum += row[col_index]
    return column_sum

def get_row_average(matrix, row_index):
    row = matrix[row_index]
    row_average = sum(row) / len(row)
    return row_average

matrix = generate_random_matrix(3, 4)

print("Generated Matrix:")
for row in matrix:
    print(row)

column_sum = get_column_sum(matrix, 1)
print("\nSum of second column:", column_sum)

row_average = get_row_average(matrix, 0)
print("Average of first row:", row_average)
