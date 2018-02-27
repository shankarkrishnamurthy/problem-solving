class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dm = { '2': 'abc', '3': 'def', '4': 'ghi','5':'jkl', '6':'mno','7':'pqrs','8':'tuv','9':'wxyz' }

        def do_combo(ds, anc):
            print("ds ", ds, " anc ", anc);
            if len(ds)==0:
                self.results.append(anc)
                return

            for l in dm[ds[0]]:
                do_combo(ds[1:], anc + l)
        
        self.results = []
        do_combo(digits[:],'') 
        return self.results
        
print(Solution().letterCombinations('2'))
print(Solution().letterCombinations('32'))
