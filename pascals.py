def Pval(l,i):
    return l[i:i+1][0] if (i >=0 and len(l) > i) else 0
    
def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    ptri = ref = [1]
    for r in range(1,rowIndex+1):
        i=0
        ptri = []
        while i < r+1:
            ptri.append(Pval(ref,i-1) + Pval(ref, i))
            i += 1
        ref = ptri
    return ptri

print getRow(0)
print getRow(1)
print getRow(2)
print getRow(3)
print getRow(4)
print getRow(5)
