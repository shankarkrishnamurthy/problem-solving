import numpy as np
class Solution:
    def setZeroes(self, matrix):
        c,r=set(),set()
        for i,row in enumerate(matrix):
            for j,v in enumerate(row):
                if v == 0: 
                    c.add(j)
                    r.add(i)
        for j in c:
            for i in range(len(matrix)):
                matrix[i][j] = 0

        for i in r:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        print(np.array(matrix))
        
Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
