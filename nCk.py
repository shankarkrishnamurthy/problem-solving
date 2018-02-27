def combo(n,k):
    def do_combo(nl, k, anc):
        if k == 0:
            res.append(anc)
            return
            
        for i in range(len(nl)):
            do_combo(nl[i+1:], k-1, anc + [nl[i]])

    res = []
    if k > 0 and n >= k: 
        do_combo([x for x in range(1,n+1)], k, [])
    return res

print combo(0,0)
print combo(1,0)
print combo(1,2)
print combo(1,1)
print combo(4,2)
    
