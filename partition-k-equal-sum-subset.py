class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        nums.sort()
        #print nums,k
        s = sum(nums)
        if s % k != 0: return False
        es = s/k
        ssh = {}
        for i,v in enumerate(nums):
            for ss,val in ssh.items():
                if ss+v > es: continue
                #print ss,v,ssh[ss]
                ssh[ss+v] = ssh.get(ss+v, []) + [x.union(set([i])) for x in val]
            if v > es: continue
            ssh[v] = ssh.get(v,[]) + [set([i])]
            #print ssh,i,v
        if not es in ssh or len(ssh[es]) < k: return False
        #print ssh[es]
        if not set(range(len(nums))) - set.union(*ssh[es]): 
            ll = []
            for i in ssh[es]:
                for l in list(ll):
                    if set.union(*l).intersection(i): continue
                    else: 
                        ll.append(l[:])
                        l.append(i)
                ll.append([i])
            for i in ll:
                if len(set.union(*i)) == len(nums):
                    return True
            return False
        return False
    


print Solution().canPartitionKSubsets([2,2,2,2,3,5],4)
print Solution().canPartitionKSubsets([4,3,2,3,5,2,1],4)
print Solution().canPartitionKSubsets([1,2,3,4],3)
print Solution().canPartitionKSubsets([4,4,6,2,3,8,10,2,10,7],4)
print Solution().canPartitionKSubsets([1,2,2,2],3)
print Solution().canPartitionKSubsets([1,2,2,2,2],3)
print Solution().canPartitionKSubsets([1, 1, 1, 3, 5, 5, 6, 6, 8, 8] ,4)
