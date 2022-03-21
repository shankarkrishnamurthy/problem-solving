from bisect import bisect as br
class Solution:
    def kIncreasing(self, arr, k):
        lis = []
        for i in range(k):
            tmp = []
            for j in range(i,len(arr),k):
                a = arr[j]
                if not tmp or tmp[-1] <= a:
                    tmp.append(a)
                else:
                    m = br(tmp, a)
                    tmp[m] = a
            lis.append(len(tmp))
        #print(lis)
        return len(arr) - sum(lis)
