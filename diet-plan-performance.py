class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        res = 0
        if len(calories) <= k: 
            if sum(calories) > upper: res=1
            elif sum(calories) < lower: res=-1
            else: pass
            return res

        for i in xrange(1,len(calories)):
            calories[i] += calories[i-1]

        calories = [0] + calories
        #print calories
        for i in xrange(k,len(calories)):
            #print i,res
            s = calories[i] - calories[i-k]
            if s > upper: res+=1
            elif s < lower: res-=1
            else: pass
        return res
        
print Solution().dietPlanPerformance(calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3)
print Solution().dietPlanPerformance(calories = [3,2], k = 2, lower = 0, upper = 1)
print Solution().dietPlanPerformance(calories = [6,5,0,0], k = 2, lower = 1, upper = 5)
