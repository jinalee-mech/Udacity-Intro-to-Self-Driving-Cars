import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        

        
        if self.h == 1:
            det = self.g[0][0]
        else :
            det = self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
        
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")


        
        result = 0
        for i in range(self.h):
            result += self.g[i][i]
            
        return result

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")


        inverse = []
    



        if self.h == 1:
            inverse.append([1 / self.g[0][0]])
        elif self.h == 2:

            if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                raise ValueError('The matrix is not invertible.')
            else:

                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]
            
                factor = 1 / (a * d - b * c)
            
                inverse = [[d, -b],[-c, a]]
            
                for i in range(len(inverse)):
                    for j in range(len(inverse[0])):
                        inverse[i][j] = factor * inverse[i][j]
    
        return Matrix(inverse)
        

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """

        matrix_transpose = []

        for c in range(self.h):
            new_row = []

            for r in range(self.h):

                new_row.append(self.g[r][c])
            matrix_transpose.append(new_row)
    
        return Matrix(matrix_transpose) 
    
        

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 

        
        result = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j]+other.g[i][j])
            result.append(row)
        return Matrix(result)
                
                
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """

        result = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-self.g[i][j])
            result.append(row)
                
        
        return Matrix(result)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """

        result = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j]-other.g[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """

        def get_row(matrix, row):
            return matrix[row]
        
        def get_column(matrix, column_number):
            column = []
            
            for r in range(len(matrix)):
                column.append(matrix[r][column_number])

            return column
        

        
        
        result = []

    

        for r in range(self.h):

            row_result = []

            rowA = get_row(self.g, r)
        
            for c in range(other.w):

                colB = get_column(other.g, c)
                
                dot_prod = 0
                
                for i in range(len(colB)):
                    dot_prod += rowA[i] * colB[i]
                               

                row_result.append(dot_prod)
    

            result.append(row_result)
        

        return Matrix(result)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass

        result = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j]*other)
            result.append(row)
        return Matrix(result)
            
            
