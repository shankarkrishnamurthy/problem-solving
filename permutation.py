def do_permute(prim, e):
    nlist = []
    for i in prim:
        tmp = list(i)
        for j in range(0,len(i)+1):
            nlist.append(tmp[:j]+[e]+tmp[j:])
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

#print(permute([1]))
#print(permute([1,2]))
#print(permute([1,2,3]))
print(permute([1,2,3,4,5]))
