def findLongestChain(pairs):
    pairs.sort(key=lambda x: x[1]) # sort on first element
    count = 0
    for ele in pairs:
        if (count ==0 or (count and ele[0] > cl[1])):
            cl = ele
            count += 1
            
    return count
    
print findLongestChain([[1,2], [3,5], [3,4], [5,6]])
print findLongestChain([[1,2], [2,3],[3,4]])
print findLongestChain([[1,2], [2,3]])
print findLongestChain([[1,2]])
print findLongestChain([])
