class Solution:
    def spiralOrder(self, mat):
        m, n, sd, q, d, ans, v = len(mat), len(mat[0]), 0, [(0,0)],[(0,1),(1,0),(0,-1),(-1,0)], [], set()
        while q:
            a,b = q.pop()
            v.add((a,b))
            x, y = a+d[sd][0],b+d[sd][1]
            if 0<=x<m and 0<=y<n and (x,y) not in v:
                ans.append(mat[a][b])
                q.append((x,y))
                continue
            sd = (sd+1) % 4
            q.append((a,b))
            if len(ans) == m*n-1: 
                ans += [mat[a][b]]
                break

        return ans

        

print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(Solution().spiralOrder([[1,2]]))
print(Solution().spiralOrder([[1]]))
