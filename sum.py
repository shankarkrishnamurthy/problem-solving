def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {k: v for v, k in enumerate(nums)}
    i = 0
    l = len(nums)
    while i < l:
        j = target - nums[i]
        try:
            if i != d[j]:
                return [i, d[j]]
        else:
            i+=1


a=[];
a = twoSum([3,2,4], 6)
print a

"""
        i=0
        l = len(nums)
        while i < l:
            sec = target - nums[i]
            i+=1
            if sec in nums:
                j=nums.index(sec)
            else:
                continue
            if (i-1) == j:
                continue
            return [i-1, j]
"""
