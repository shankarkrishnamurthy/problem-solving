class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        orign = len(matrix)
        if not orign: return False
        origm = len(matrix[0])
        if not origm: return False
        print matrix, "row ", orign, "col ",origm
        def do_search(bi,bj,n,m):
            i, j = bi, bj
            print i,j,n,m
            while i < n or j < m:
                if matrix[i][j] == target: return True
                if target > matrix[i][j]:
                    i += 1
                    j += 1    
                    if j == m and i == n: return False
                    if i == n: i = bi
                    if j == m: j = bj
                else:
                    if abs(bi-n) < 2 or abs(bj-m) < 2: return False
                    return do_search(bi,j,i,m) or do_search(i,bj,n,j)
            return False
        return do_search(0,0,orign,origm)
        
#print Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)
#print Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
#print Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19]], 13)
#print Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19]], 15)
#print Solution().searchMatrix([[1]], 1)
#print Solution().searchMatrix([[2,3]], 3)
#print Solution().searchMatrix([[2],[3]], 3)
#print Solution().searchMatrix([[]], 15)
#print Solution().searchMatrix([], 0)
#print Solution().searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],15)
#print Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],12)
print Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20)
