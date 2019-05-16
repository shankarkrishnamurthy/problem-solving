class Solution(object):
    def isRobotBounded(self, m):
        """
        :type instructions: str
        :rtype: bool
        """
        h = []
        L = {'N': 'W', 'W':'S', 'S':'E', 'E':'N' }
        R = {'N': 'E', 'W':'N', 'S':'W', 'E':'S' }
        c, d = [0,0], 'N'
        h.append(tuple(c))
        for i in xrange(4):
            for j in m:
                if j == 'L':
                    d = L[d]
                elif j == 'R': 
                    d = R[d]
                else:
                    if d == 'N': c[1] += 1
                    elif d == 'S': c[1] -= 1
                    elif d == 'W': c[0] -= 1
                    else: c[0] += 1
                    h.append(tuple(c))
            print h
            if tuple(c) == h[0]: return True
        return False

print Solution().isRobotBounded("GGLLGG")
print Solution().isRobotBounded("GG")
print Solution().isRobotBounded("GL")
