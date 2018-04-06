import matrixChain



def recurseMultiply(matrix_chain, cross, soln):
    if len(matrix_chain) == 1:
        return matrix_chain[0].matrix
    if len(matrix_chain) == 2:
        return Matrix.multiplyM(matrix_chain[0].matrix, matrix_chain[1].matrix)


    cross_left = soln[(0,cross-1)]
    cross_right = soln[(cross, len(matrix_chain)-1)]
    left = recurseMultiply(matrix_chain[:cross], cross_left, soln)   # recurse always return a matrix
    right = recurseMultiply(matrix_chain[cross:], cross_right, soln)

    return Matrix.multiplyM(left, right)  # mismatched type


class Matrix_Chain:


    def __init__(self):
        self.chain = []

    def insert(self, matrix): # matrix is a class Matrix
        self.chain.append(matrix)

    def getDimArray(self):
        dimArr = []
        for matrix in self.chain:
            dim = (matrix.row, matrix.col)
            dimArr.append(dim)
        return dimArr

    def getSubChain(self, begin, end):
        return self.chain[begin: end+1]


class Matrix:
    def __init__(self, arr):
        self.matrix = arr
        self.row = len(arr)
        self.col = len(arr[0])



    def printM(self):
        for row in self.matrix:
            print(row)

    @staticmethod
    def multiplyM(A, B):
        C = []

        for i in range(len(A)):  # i from i=1 to i = # of rows of A
            new_row = []
            for j in range(len(B[0])):  # iterate over column of B
                new_elem = 0
                for k in range(len(A[0])):
                    new_elem += A[i][k] * B[k][j]
                new_row.append(new_elem)
            C.append(new_row)
        return C



A = Matrix([
    [0,1,2],
    [3,4,5],
]) # (2,3)

B = Matrix([
    [1,2,3,4],
    [5,6,7,8],
    [10,11,-1,2]


]) # (3,4)

C = Matrix([
    [-1],
    [12],
    [16],
    [7]
]) # (4,1)

D = Matrix([
    [-9, 69, 12, 5, 32]

])

chain = Matrix_Chain()  # create class
chain.insert(A)
chain.insert(B)
chain.insert(C)
chain.insert(D)

dimArr = chain.getDimArray()

MIN_VAL, MIN_DIM, soln = matrixChain.topDown(dimArr, 0, len(dimArr)-1)
cross = soln[(0,len(dimArr)-1)]


print(chain.chain)
print(cross)
print(MIN_VAL)

for i in range(len(chain.chain)):
    soln[(i,i)] = None

result = Matrix(recurseMultiply(chain.chain, cross, soln))

result.printM()
# print(A)
# chain = Matrix_Chain()
# chain.insert(A)
# chain.insert(B)
# dimArr = chain.getDimArray()
# print(dimArr)
# MIN_VAL, MIN_DIM, soln = matrixChain.topDown(dimArr, 0, len(dimArr)-1)
# print(soln)
# print(chain.chain)
# print(chain.getSubChain(0,1))
# print(multiplyM(A.matrix,B.matrix))