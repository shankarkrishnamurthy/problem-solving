class Solution:
    def countSubarrays(self, nums, k):
        ps, res, l, cs = [0]*len(nums), 0, 0, 0
        for i,v in enumerate(nums):
            cs += v
            ps[i] = cs
            while l <= i:
                ss, sl = (cs-ps[l-1] if l > 0 else cs), i-l+1
                #print('i', i, 'l', l, 'score', sl*ss, 'k', k, 'length', sl)
                if sl*ss < k: 
                    res += sl
                    break
                else: l+=1
        return res
