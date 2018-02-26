class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def do_exist(anc, w, b):
            if len(w) == 0:
                print anc
                return True
            (r,c) = anc[-1]
            l = []
            if r+1 < len(b) and (r+1,c) not in anc and b[r+1][c] == w[0]:
                l += [(r+1,c)]
            if r-1 >= 0 and (r-1,c) not in anc and b[r-1][c] == w[0]:
                l += [(r-1,c)]
            if c+1 < len(b[0]) and (r,c+1) not in anc and b[r][c+1] == w[0]:
                l += [(r,c+1)]
            if c-1 >= 0 and (r,c-1) not in anc and b[r][c-1] == w[0]:
                l += [(r,c-1)]
            for i in l:
                if True == do_exist(anc+[i], w[1:], b):
                    return True

            return False

        if not len(word):
            return ex
        l = [(r,c) for r in range(len(board)) for c in range(len(board[r])) if word[0] == board[r][c]]
        print l
        for item in l:
            if True == do_exist([item], word[1:], board):
                return True
        return False

print Solution().exist([ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "ABCCED")
print Solution().exist([ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "SEE")
print Solution().exist([ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "ABCB")
