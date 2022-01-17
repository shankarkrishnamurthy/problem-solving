class Solution:
    def validArrangement(self, pairs):
        def walk(n):
            q, res,ans = [n], [], []
            while q:
                i = q.pop()
                if i not in e or len(e[i])==0:
                    if not res: break
                    ele = res.pop()
                    ans.append(ele)
                    q.append(pairs[ele][0])
                    continue
                
                k = e[i].pop()
                q.append(pairs[k][1])
                res.append(k)
            return [pairs[i] for i in ans[::-1]]
            
        e, f  = {},{}
        for i,(p,q) in enumerate(pairs):
            e.setdefault(p,[]).append(i)
            f[p] = f.get(p,0) + 1
            f[q] = f.get(q,0) - 1
        #print(' pairs ', pairs)
        #print(' e ', [(i,e[i]) for i in sorted(e)], '\n f ',[(i,f[i]) for i in sorted(f)])
        for i in f:
            if f[i] > 0: return walk(i)
        return walk(pairs[0][0])


print(Solution().validArrangement([[5,1]]))
print(Solution().validArrangement([[5,1],[4,5],[11,9],[9,4]]))
print(Solution().validArrangement([[3,2],[2,1],[1,3]]))
print(Solution().validArrangement([[1,2],[1,3],[2,1]]))
print(Solution().validArrangement([[8,5],[8,7],[0,8],[0,5],[7,0],[5,0],[0,7],[8,0],[7,8]]))
print(Solution().validArrangement([[5,13],[10,6],[11,3],[15,19],[16,19],[1,10],[19,11],[4,16],[19,9],[5,11],[5,6],[13,5],[13,9],[9,15],[11,16],[6,9],[9,13],[3,1],[16,5],[6,5]]))
#print(Solution().validArrangement([[229,699],[489,928],[92,398],[457,398],[798,838],[75,547],[856,141],[838,141],[356,578],[819,537],[229,458],[229,838],[473,175],[545,826],[705,75],[132,262],[92,974],[141,547],[856,92],[229,856],[838,826],[798,15],[892,157],[578,229],[458,905],[141,856],[157,458],[157,489],[92,458],[838,699],[905,458],[547,798],[928,157],[974,15],[545,132],[545,15],[141,132],[458,175],[856,586],[175,705],[547,229],[928,771],[157,671],[175,473],[132,229],[838,671],[458,356],[262,838],[75,262],[92,798],[156,671],[356,124],[547,175],[262,457],[705,545],[671,156],[928,671],[578,892],[483,856],[586,141],[141,838],[974,928],[356,157],[398,586],[15,157],[905,175],[856,157],[157,856],[398,771],[892,586],[974,473],[262,458],[175,141],[458,92],[175,856],[905,974],[928,229],[826,699],[826,483],[826,905],[905,838],[928,356],[974,905],[124,356],[124,537],[771,545],[262,771],[157,928],[229,157],[547,141],[928,75],[262,974],[856,798],[92,132],[15,141],[141,819],[458,15],[141,905],[458,928],[537,586],[92,819],[473,262],[578,473],[141,458],[15,856],[132,798],[537,974],[586,398],[928,141],[141,262],[771,141],[458,974],[157,771],[398,175],[838,974],[826,92],[175,892],[974,157],[838,356],[699,229],[356,489],[15,771],[771,905],[586,92],[771,92],[798,826],[92,537],[699,458],[671,928],[771,928],[398,928],[699,157],[458,157],[537,905],[974,578],[671,92],[671,75],[157,75],[156,838],[473,398],[928,705],[15,458],[705,458],[157,15],[819,124],[157,92],[699,928],[905,699],[798,262],[458,547],[586,856],[974,489],[856,545],[75,974],[75,578],[905,826],[856,705],[489,547]]))
