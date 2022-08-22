class Solution:
    def countCollisions(self, dirn):
        ncol, lw, wmr = 0, 0, 0
        for d in dirn:
            if d == "L":
                if wmr > 0: lw = 1
                if lw: ncol, wmr = ncol + 1 + wmr, 0
            elif d == "R": wmr += 1
            else: ncol, wmr, lw = ncol + wmr, 0, 1
            #print('dir', d, 'wmr', wmr, 'ncol', ncol, 'lw', lw)
        return ncol
