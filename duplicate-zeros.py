class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        l, r = 0, len(arr)-1
        while l < r:
            if arr[l] == 0: r -= 1
            l += 1

        print 'Before ',arr, r, 'len ', len(arr), 'cnt ', arr[:r+1].count(0), ' last ', arr[r]
        i = len(arr) - 1
        c = arr[:r+1].count(0)
        if (len(arr) - r+1-c) % 2 == 1:
            arr[i] = arr[r]
            i -= 1
            r -= 1
        while i > r and r >= 0:
            if arr[r] == 0:
                arr[i] = 0
                i -= 1
            arr[i] = arr[r]
            i -= 1
            r -= 1
        print 'After ', arr
        
print Solution().duplicateZeros([9,9,9,4,8,0,0,3,7,2,0,0,0,0,9,1,0,0,1,1,0,5,6,3,1,6,0,0,2,3,4,7,0,3,9,3,6,5,8,9,1,1,3,2,0,0,7,3,3,0,5,7,0,8,1,9,6,3,0,8,8,8,8,0,0,5,0,0,0,3,7,7,7,7,5,1,0,0,8,0,0])
print Solution().duplicateZeros([1,0,2,3,0,4,5,0])
print Solution().duplicateZeros([1,2,3])
print Solution().duplicateZeros([0])
print Solution().duplicateZeros([0,0])
print Solution().duplicateZeros([1])
print Solution().duplicateZeros([1,2,3,0])
print Solution().duplicateZeros([1,2,3,0,0])
