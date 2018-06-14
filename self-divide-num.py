class Solution(object):
    def selfDividingNumbers(self, left, right):
        res = []
        for n in range(left,right+1):
            yes = 1
            for d in str(n):
                if not int(d) or n % int(d) != 0:
                    yes = 0
                    break
            if yes: res.append(n) 
        return res

print Solution().selfDividingNumbers(22,44)
