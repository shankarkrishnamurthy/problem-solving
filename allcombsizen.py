def allsubssizen(nl, sz):
    res = [[]]
    for i in nl:
        c=[]
        for e in res:
            if len(e) == sz: continue
            c += [e + [i]]
        res += c
    print('len', len(res))
    return res
#print(allsubssizen([1,2,3], 1))
#print(allsubssizen([1,2,3,4], 2))
print(allsubssizen(range(15), 2))
