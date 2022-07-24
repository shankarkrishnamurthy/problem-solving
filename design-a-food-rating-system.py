class FoodRatings:
    def __init__(o, f, c, r):
        o.fh, o.c = defaultdict(int), defaultdict(list)
        for i in range(len(f)):
            o.fh[f[i]] = [r[i], c[i]]
            heappush(o.c[c[i]], (-r[i], f[i]))

    def changeRating(o, f, nr):
        r, c = o.fh[f]
        o.fh[f] = [nr, c]
        heappush(o.c[c], (-nr, f))
        topr, topf = o.c[c][0]
        while -o.fh[topf][0] != topr:
            heappop(o.c[c])
            topr, topf = o.c[c][0]
        
    def highestRated(o, c):
        return o.c[c][0][1]
