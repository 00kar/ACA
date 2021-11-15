class Solution:
    def transpose(self, matrix):
        matrix_T = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
        
        return matrix_T



ini = [[1,2,3],[4,5,6],[7,8,9]]

s = Solution().transpose(ini)

print('\tinitial matrix')
for i in ini: print(i)

print('\ttranpose matrix')
for i in s: print(i)
