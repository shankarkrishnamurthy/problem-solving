class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.results = []
        def do_combo(nl, anc, target):
            print(nl, " ", anc, " ", target)
            for i in range(0,len(nl)):
                for j in range(1,int(target/nl[i])+1):
                    nt = target - nl[i]*j
                    if nt == 0:
                        self.results.append(sorted(anc+[nl[i]]*j))
                        print("Ans: ", self.results[-1])
                    elif nt > 0 and len(nl) > 1:
                        tl = nl[i+1:]
                        if len(tl) > 0 and not tl[0] > nt:
                            do_combo(tl, anc+[nl[i]]*j, nt)
                    else:
                        continue
            
        candidates.sort()
        print("candidates: ", candidates)
        do_combo(candidates[:], [], target)
        return self.results

print("Ans: ",Solution().combinationSum([1],1))
print("Ans: ",Solution().combinationSum([1],2))
print("Ans: ",Solution().combinationSum([2, 3, 6, 7,9],7))
print("Ans: ",Solution().combinationSum([4,7,2,9],15))
