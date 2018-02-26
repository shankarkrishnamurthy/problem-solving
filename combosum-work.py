import itertools as it
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = []
        c = min(candidates)
        candidates += [c]*(int(target/c)-1)
        candidates[:] = it.filterfalse(lambda x: x> target, candidates)
        print("candidates ", candidates)
        n = len(candidates)
        for k in range(1,n+1):
            l += [sorted(i) for i in it.combinations_with_replacement(candidates, k) if sum(i) == target]
        return list(list(j) for j in set(tuple(i) for i in l))

print(Solution().combinationSum([2, 3, 6, 7,9],7))
print(Solution().combinationSum([1],1))
print(Solution().combinationSum([1],2))
print(Solution().combinationSum([4,7,2,9],15))
