class Solution:
    def countBadPairs(self, nums):
        n, tp, ph = len(nums), 0, defaultdict(int)
        for i,v in enumerate(nums):
            if v-i in ph: tp += ph[v-i]
            ph[v-i] += 1
        #print(ph, 'tp', tp)
        return n*(n-1)//2 - tp
        
