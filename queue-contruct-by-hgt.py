class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people: return people
        sll = sorted(people, key=lambda x: (x[0],-x[1]), reverse=True)
        res = []
        for i in range(len(sll)):
            res.insert(sll[i][1], sll[i])
            #print res
        
        return res
        
ll = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print Solution().reconstructQueue(ll)
ll=[[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
print Solution().reconstructQueue(ll)
ll = [[5,0]]
print Solution().reconstructQueue(ll)
ll = [[4,1],[5,0]]
print Solution().reconstructQueue(ll)
ll = [[5,1],[5,0]]
print Solution().reconstructQueue(ll)
