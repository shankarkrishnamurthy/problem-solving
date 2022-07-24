class NumberContainers:
    def __init__(o):
        o.ih, o.mi = defaultdict(int), defaultdict(list)

    def change(o, i, n):
        on = o.ih[i]
        o.ih[i] = n
        heappush(o.mi[n], i)
        while o.mi[on]:
            if o.ih[o.mi[on][0]] != on: heappop(o.mi[on])
            else: break
            
    def find(o, n):
        #print(dict(o.ih), dict(o.mi))
        if n not in o.mi or not o.mi[n]: return -1
        return o.mi[n][0]
