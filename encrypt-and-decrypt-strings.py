
class Encrypter:
    def __init__(o, k, v, d):
        o.km, o.dw, o.v = {}, {}, v
        for i in range(len(k)): o.km[k[i]] =  i
        for w in d:
            ew = o.encrypt(w)
            o.dw[ew] = o.dw.get(ew, 0) + 1

    def encrypt(o, w1):
        res = ""
        for c in w1: res += o.v[o.km[c]]
        return res

    def decrypt(o, w2):
        return (o.dw[w2] if w2 in o.dw else 0)

