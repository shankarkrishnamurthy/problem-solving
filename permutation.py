def do_permute(prim, e):
    nlist = []
    for i in prim:
        for j in range(0,len(i)+1):
            tmp = list(i)
            tmp.insert(j, e)
            nlist += [tmp]
    return nlist
    
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    l1 = []
    for e in nums:
        if not l1:
            l1 = [[e]]
            continue
        l1 = do_permute(l1, e)
    return l1

print permute([1])
print permute([1,2])
print permute([1,2,3])
#print permute([1,2,3,4,5])
