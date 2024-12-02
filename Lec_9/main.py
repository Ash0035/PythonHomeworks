import random


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to add.")
        result = Matrix(self.rows, self.cols)
        result.data = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to subtract.")
        result = Matrix(self.rows, self.cols)
        result.data = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError(
                "The number of columns in the first matrix must equal the number of rows in the second."
            )
        result = Matrix(self.rows, other.cols)
        result.data = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return result


matrix1 = Matrix(3, 3)
matrix2 = Matrix(3, 3)

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix 1 + Matrix 2:")
print(matrix1 + matrix2)

print("\nMatrix 1 - Matrix 2:")
print(matrix1 - matrix2)

matrix3 = Matrix(3, 2)
matrix4 = Matrix(2, 3)

print("\nMatrix 3:")
print(matrix3)

print("\nMatrix 4:")
print(matrix4)

print("\nMatrix 3 * Matrix 4:")
print(matrix3 * matrix4)
