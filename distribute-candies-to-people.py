class Solution(object):
    def distributeCandies(self, c, n):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        i, k, ans = 1, 1, [0]*n
        ans[0] = 1
        c -= 1
        while c > 0:
            k += 1
            if c >= k: c -= k
            else: 
                k = c
                c = 0
            ans[i%n] += k
            i += 1
            #print i, ans

        #print sum(ans)
        return ans
        

print Solution().distributeCandies(10**9, 1000)
print Solution().distributeCandies(100, 7)
#print Solution().distributeCandies(1, 1)
#print Solution().distributeCandies(10, 3)
#print Solution().distributeCandies(7, 4)
