def dynLongChain(pairs, idx, cl):
    # We can use the item in idx or not
    # max of resulting answer
    while (len(cl) and idx < len(pairs) and cl[-1][1] >= pairs[idx][0]): 
        idx += 1

    if idx >= len(pairs):
        return cl

    v1 = dynLongChain(pairs, idx+1, cl[:])
    cl.append(pairs[idx])
    v2 = dynLongChain(pairs, idx+1, cl[:])
    return v1 if len(v1) > len(v2) else v2

def dynLongChainLen(pairs, idx, cl):
    # We can use the item in idx or not
    # max of resulting answer
    while (len(cl) and idx < len(pairs) and cl[-1][1] >= pairs[idx][0]): 
        idx += 1

    if idx >= len(pairs):
        return len(cl)

    v1 = dynLongChainLen(pairs, idx+1, cl[:])
    cl.append(pairs[idx])
    v2 = dynLongChainLen(pairs, idx+1, cl[:])
    return max(v1,v2)
    
def findLongestChain(pairs):
    pairs.sort() # sort on first element

    return dynLongChainLen(pairs, 0, [])
    
print findLongestChain([[1,2], [3,5], [3,4], [5,6]])
print findLongestChain([[1,2], [2,3],[3,4]])
print findLongestChain([[1,2], [2,3]])
print findLongestChain([[1,2]])
print findLongestChain([])
