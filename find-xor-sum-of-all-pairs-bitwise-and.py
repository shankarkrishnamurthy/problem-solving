class Solution:
    def getXORSum(self, arr1, arr2):
        h1, h2, res = [0]*32,[0]*32,0
        for i in range(max(len(arr1), len(arr2))):
            for j in range(32):
                if i < len(arr1) and arr1[i] & (1<<j): h1[j] += 1
                if i < len(arr2) and arr2[i] & (1<<j): h2[j] += 1
        for k in range(32):
            if (h1[k]*h2[k]) % 2 == 1: res |= 1<<k
        return res
