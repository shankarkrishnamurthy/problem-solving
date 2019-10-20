class Solution:
    def minimumAbsDifference(self, arr: 'List[int]') -> 'List[List[int]]':
        arr.sort()
        dsf = 2000001
        ans = []
        for i in range(1,len(arr)):
            cd = arr[i] - arr[i-1]
            if cd < dsf:
                ans = [[arr[i-1],arr[i]]]
                dsf = cd
            elif cd == dsf:
                ans.append([arr[i-1],arr[i]])
            
        return ans

print(Solution().minimumAbsDifference([4,2,1,3]))
print(Solution().minimumAbsDifference([1,3,6,10,15]))
print(Solution().minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
