class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        print matrix
        m = len(matrix)
        n = len(matrix[0])
        t = m if m > n else n
        for i in range(t):
            j,udval,ldval = 0,100,100
            print 'Next Diagonal ', i
            while j < m:
                x = j
                y = i+j
                if y < n and x < m:
                    if  udval == 100: 
                        print 'setting udval', x,y, udval
                        udval = matrix[x][y]
                    print x,y, udval
                    if matrix[x][y] != udval: return False
                if y < m and x < n:
                    if ldval == 100: 
                        print 'setting ldval', y,x, ldval
                        ldval = matrix[y][x]
                    print y,x, ldval
                    if matrix[y][x] != ldval: return False

                j+=1
        return True
        
print Solution().isToeplitzMatrix([[41,45],[81,41],[73,81],[47,73],[0,47],[79,76]])
#print Solution().isToeplitzMatrix([[0,33,98],[34,22,33]])
#print Solution().isToeplitzMatrix([ [1,2,3,4], [5,1,2,3], [9,5,1,2] ])
#print Solution().isToeplitzMatrix([ [1,2], [2,2] ])

