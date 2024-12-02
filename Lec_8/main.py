import random


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
        return sum(map(sum, self.matrix)) / (self.n * self.m)

    def sum_of_row(self):
        row_index = int(input("Enter the row index (0-based): "))
        return sum(self.matrix[row_index])

    def average_of_column(self):
        col_index = int(input("Enter the column index (0-based): "))
        return sum(row[col_index] for row in self.matrix) / self.n

    def print_submatrix(self):
        col1, col2 = map(int, input("Enter column range (col1 col2): ").split())
        row1, row2 = map(int, input("Enter row range (row1 row2): ").split())
        for row in self.matrix[row1:row2]:
            print(row[col1:col2])


matrix = Matrix(5, 6)

print("Matrix:")
matrix.print_matrix()

print("\nMean of the matrix:", matrix.calculate_mean())
print("\nSum of a selected row:", matrix.sum_of_row())
print("\nAverage of a selected column:", matrix.average_of_column())

print("\nSubmatrix:")
matrix.print_submatrix()