class LUPrefix:
    def __init__(o, n):
        o.q, o.l = [0]*(n+2), 1

    def upload(o, v):
        o.q[v] = 1
        while o.q[o.l] != 0: o.l += 1

    def longest(o):
        return o.l-1
