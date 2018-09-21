class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if len(tree) < 3: return len(tree)
        basket, ans = {tree[0]: 1},1
        for i in range(1,len(tree)):
            if tree[i] in basket:
                basket[tree[i]] += 1
                if tree[i] != tree[i-1]: chg = i
            else:
                if len(basket) == 1:
                    basket[tree[i]] = 1
                else:
                    x,y = basket.keys()
                    if x == tree[i-1]:
                        del basket[y]
                    else:
                        del basket[x]
                    basket[tree[i]] = 1
                    basket[tree[i-1]] = i - chg
                chg = i
            #print i, cres, basket
            ans = max(sum(basket.values()), ans)
        return ans

print Solution().totalFruit([1,0,1,4,1,4,1,2,3])
print Solution().totalFruit([0,1,6,6,4,4,6])
print Solution().totalFruit([0])
print Solution().totalFruit([0,0])
print Solution().totalFruit([0,1])
print Solution().totalFruit([1,2,1])
print Solution().totalFruit([0,1,2,2])
print Solution().totalFruit([1,2,3,2,2])
print Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4])
