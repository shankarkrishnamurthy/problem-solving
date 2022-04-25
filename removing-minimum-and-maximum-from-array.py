class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = nums.index(min(nums)), nums.index(max(nums))
        if a > b : a,b = b,a
        #print('a',a,'b',b, 'n', n)
        return min(a + 1 + (b-a), n-b + b-a, a + 1 + n-b)
