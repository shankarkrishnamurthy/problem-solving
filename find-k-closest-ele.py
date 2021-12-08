from bisect import *
class Solution:
    def findClosestElements(self, arr, k, x):
        res , i = [], bisect_left(arr,x)
        #print ( "input", arr, k, x, i)
        c, l, r = 0, i-1, i
        
        while c < k:
            if l < 0:
                res += arr[r:r+k-c]
                break
            if r >= len(arr):
                res += arr[l-(k-c)+1:l+1]
                break
            if abs(x - arr[l]) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            c += 1
            #print('l=',l,'r=',r, res)

        res.sort()
        return res

print(Solution().findClosestElements([-2,-1,1,2,3,4,5],7,3))
print(Solution().findClosestElements([1], 1, 3))
print(Solution().findClosestElements([4, 7], 1, 5))
print(Solution().findClosestElements([4, 7], 1, 6))
print(Solution().findClosestElements([4, 7], 2, 5))
print(Solution().findClosestElements([1,2,3,4,5], 4, 3))
print(Solution().findClosestElements([1,2,3,4,5], 4,-1))
