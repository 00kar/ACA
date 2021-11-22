from copy import deepcopy

class Matrix:
    def __init__(self, *args, **kwargs):
        """
        Takes 2 keyword arguments: filename or list. If filename is given
        read the matrix from file. Else, read it directly from list.
        """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])

    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            matrix_list = f.readlines()
        matrix_list = list(map(lambda s: list(map(float, s[:-1].split(' '))), matrix_list))
        self.read_as_list(matrix_list)

    def __str__(self):
        s = '---------MATRIX---------\n'
        s += '\n'.join(str(row) for row in self._matrix)
        s += '\n'
        s += f'colums = {self.shape[0]}\nrows = {self.shape[1]}'
        s += '\n------------------------\n'
        return s

    def write_to_file(self, filename):
        """
        Write the matrix to the given filename.
        TODO: implement
        """
        with open(filename, 'a+') as f:
            f.write('\n'.join(self._matrix))

    def traspose(self):
        """
        Transpose the matrix.
        TODO: implement
        """
        return Matrix(list = [[self._matrix[i][j] for i in range(self.shape[1])] for j in range(self.shape[0])])

    @property
    def shape(self):
        return self._columns, self._rows

    def __add__(self, other):
        """
        The `+` operator. Sum two matrices.
        TODO: implement
        """
        if isinstance(other, Matrix):
            if self.shape == other.shape:
                return Matrix(list = [[self._matrix[i][j] + other._matrix[i][j]  for j in range(self.shape[0])] for i in range(self.shape[1])])
            else:
                raise ValueError("Shapes are inappropirate!")
        else:
            raise TypeError("Expected a <class '__main__.Matrix'>  object")

    def __mul__(self, other):
        """
        The `*` operator. Element-wise matrix multiplication.
        Columns and rows sizes of two matrices should be the same.
        If other is not a matrix (int, float) multiply all elements of the matrix to other.
        TODO: implement
        """
        if isinstance(other, (int,float)):
            return Matrix(list = [[self._matrix[i][j] * other for j in range(self.shape[0])] for i in range(self.shape[1])])
        elif isinstance(other, Matrix):
            return Matrix(list = [[self._matrix[i][j] * other._matrix[i][j] for j in range(self.shape[0])] for i in range(self.shape[1])])
        else:
            raise TypeError("Expected a <class 'int'>, <class 'float'> or <class '__main__.Matrix'>  object")

    def __matmul__(self, other):
        """
        The `@` operator. Mathematical matrix multiplication.
        The number of columns in the first matrix must be equal to the number of rows in the second matrix.
        TODO: implement
        """
        if self.shape[0] == other.shape[1]:
            return Matrix(list = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*other._matrix)] for X_row in self._matrix])
        else:
            raise ValueError('Got incorrect matrix')

    @property
    def trace(self):
        """
        Find the trace of the matrix.
        TODO: implement
        """
        if self.shape[0] == self.shape[1]:
            return sum(self._matrix[i][i] for i in range(self.shape[0]))
        else:
            raise Exception('Trace is not defined for non-square matrices!')

    @property
    def determinant(self):
        """
        Check if the matrix is square, find the determinant.
        TODO: implement
        """
        M = deepcopy(self._matrix)
        n = self.shape[1]
 
        for focusDiagonal in range(n):
            for i in range(focusDiagonal+1, n):
                if M[focusDiagonal][focusDiagonal] == 0:
                    M[focusDiagonal][focusDiagonal] == 1.0e-18
            
                currentRowScaler = M[i][focusDiagonal] / M[focusDiagonal][focusDiagonal] 

                for j in range(n): 
                    M[i][j] = M[i][j] - currentRowScaler * M[focusDiagonal][j]

        product = 1.0
        for i in range(n):
            product *= M[i][i] 
 
        return product



