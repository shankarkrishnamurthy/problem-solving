
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        s2 = set(arr2)
        a,b,ec = [], [],{}
        for i in arr1:        
            if i not in s2: b += [i]
            else:
                ec[i] = ec.get(i,0)+1
        b.sort()
        for i in arr2:
            a += [i]*ec[i]
        return a+b

print Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])
