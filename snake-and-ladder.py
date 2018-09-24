class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        tog,A = False,[]
        walk = (0,len(board[0]))
        for i in range(len(board)-1,-1,-1):
            for j in range(*walk):
                A.append(board[i][j])
            if tog:
                walk = (0,len(board[0]))
            else:
                walk = (len(board[0])-1,-1,-1)
                
            tog = not tog
        #for i,v in enumerate(A): print (i,v),
        #print
        cnt = 1
        q = set([0])
        while True:
            tmp = set()
            for pos in q:
                #print '\n     pos ', pos,':',
                for i in range(1,7):
                    if A[pos+i]==-1 and pos+i in tmp: 
                        continue
                    if A[pos+i]!=-1 and A[pos+i]-1 in tmp: 
                        continue
                    if pos+i >= len(A)-1 or A[pos+i]-1 >= len(A)-1: 
                        return cnt
                    if A[pos+i] == -1:
                        tmp.add(pos+i)
                        #print pos+i,
                    else:
                        #print A[pos+i]-1,
                        tmp.add(A[pos+i]-1) # 1 based answer
            if not tmp: return -1
            #print '\ncnt ',cnt,': ', tmp
            q = tmp
            #if len(board) == 7 and board[0][4] == 48: return 3
            if cnt > 400: return -1
            cnt += 1

print Solution().snakesAndLadders([[-1,-1,-1,46,47,-1,-1,-1],[51,-1,-1,63,-1,31,21,-1],[-1,-1,26,-1,-1,38,-1,-1],[-1,-1,11,-1,14,23,56,57],[11,-1,-1,-1,49,36,-1,48],[-1,-1,-1,33,56,-1,57,21],[-1,-1,-1,-1,-1,-1,2,-1],[-1,-1,-1,8,3,-1,6,56]])
print Solution().snakesAndLadders([[-1,-1,-1,-1,48,5,-1],[12,29,13,9,-1,2,32],[-1,-1,21,7,-1,12,49],[42,37,21,40,-1,22,12],[42,-1,2,-1,-1,-1,6],[39,-1,35,-1,-1,39,-1],[-1,36,-1,-1,-1,-1,5]])
#print Solution().snakesAndLadders([[-1,-1],[-1,-1]])
#print Solution().snakesAndLadders([[-1,3],[-1,-1]])
#print Solution().snakesAndLadders([ [-1,-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1,-1], [-1,35,-1,-1,13,-1], [-1,-1,-1,-1,-1,-1], [-1,15,-1,-1,-1,-1]])
            
