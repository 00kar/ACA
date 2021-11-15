class Solution:
    def matrixReshape(self, mat, r, c):
        line = [item for sub in mat for item in sub]
        if len(line) < c:
            line += [0]*(c-len(line))
        mat_R = []
        for i in range(r):
            mat_R.append(line[:c])
            line = line[c:] if len(line) != c else [0]*c
        return mat_R


ini = [[1,2],[3,4]]
row,col = int(input('row = ')),int(input('col = '))

s = Solution().matrixReshape(ini, row, col)

print('\tinitial matrix')
for i in ini: print(i)

print('\treshaped matrix to {}x{}'.format(row,col))
for i in s: print(i)
