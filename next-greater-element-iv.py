class Solution:
    def secondGreaterElement(self, nums):
        p, st, n = [[] for _ in range(len(nums))], [], len(nums)
        for i in range(n):
            while st and nums[st[-1]] < nums[i]:
                p[i].append(st.pop())
            st.append(i)
        hq, res = [], [-1]*n
        for i in range(n):
            while hq and hq[0][0] < nums[i]:
                res[heappop(hq)[1]] = nums[i]
            for j in p[i]:
                heappush(hq, (nums[j], j))
        return res
