def longPalin(s):
    ll = list('#'.join(s))
    Wi = []
    for idx in range(0,len(ll)):
        i = j = idx
        Wi[idx:idx] = [0] if ll[idx] != '#' else [1]
        while i>=0 and j<len(ll):
            if ll[i] == ll[j]: 
                Wi[idx] += 1
            else:
                break
            i -= 1
            j += 1
    maxidx = 0
    maxval = 0
    for i in range(0, len(Wi)):
        if Wi[i] > maxval or (Wi[i] == maxval and ll[i] != '#'):
            maxidx = i
            maxval = Wi[i]

    #print "maxidx ", maxidx, " maxval ", maxval
    #print ll
    #print Wi 
    maxval = maxval-1 if ll[maxidx] == '#' else maxval
    start = maxidx-maxval+1
    end = maxidx + maxval
    #print ll[start:end]
    lp =  ''.join(ll[start:end])
    lp = lp.replace('#','')
    return lp

print longPalin("a")
print longPalin("caa")
print longPalin("baa")
print longPalin("aba")
print longPalin("ababacabacd")
print longPalin("malayalam")
print longPalin("cbbd")
print longPalin("ccc")
print longPalin("cccc")
