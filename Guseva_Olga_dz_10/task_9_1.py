class Matrix:

    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        result_str = ''
        for st in self.matr:
            result_str += (' '.join(map(str, st)))
            result_str += '\п'
            return result_str

    def __add__(self, other):
        result_matrix = []
        if len(self.matr) == len(other.matr):
            for i in range(len(self.matr)):
                if len(self.matr[i]) == len(other.matr[i]):
                    result_matrix_stroke = [x + y for x, y in zip(self.matr[i], other.matr[i])]
                    result_matrix.append(result_matrix_stroke)
                else:
                    raise Exception('Two matrix have different size!!!')
        else:
            raise Exception('Two matrix have different size!!!')
        return Matrix(result_matrix)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[7, 1, 3], [2, 9, 1], [4, 1, 7]])
result_sum = matrix_1 + matrix_2

print(result_sum)
