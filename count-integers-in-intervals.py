from bisect import *
class CountIntervals:
    def __init__(o): o.st, o.en, o.cnt = [], [], 0

    def add(o, l, r):
        if not o.en or l > o.en[-1]+1:
            o.st.append(l), o.en.append(r)
            o.cnt += r-l+1
            return
        i, j = bisect_left(o.st, l), bisect(o.en, r)
        if i > 0 and o.st[i-1] < l <= o.en[i-1]+1: i = i-1
        if j < len(o.en)-1 and o.st[j+1]-1 <= r < o.en[j+1]: j = j+1
        c, j= 0, min(j, len(o.en)-1)
        if r < o.st[j]-1: j = j-1
        if i > j:
            nl, nr, o.cnt = l, r, o.cnt+ r-l + 1
            o.st[i:i], o.en[i:i] = [l], [r]
        else:
            for k in range(i,j+1): c += o.en[k] - o.st[k] + 1
            nl, nr = min(l, o.st[i]), max(r, o.en[j])
            o.st[i:j+1], o.en[i:j+1] = [nl], [nr]
            o.cnt += nr-nl+1 - c

    def count(o): return o.cnt
