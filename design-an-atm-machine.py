class ATM:
    def __init__(o):
        o.a=o.b=o.c=o.d=o.e=0
    def deposit(o, bnc):
        o.a,o.b,o.c,o.d,o.e = o.a+bnc[0],o.b+bnc[1],o.c+bnc[2],o.d+bnc[3],o.e+bnc[4]
        #print('deposit ', o.a,o.b,o.c,o.d,o.e)
    def withdraw(o, amt):
        an, bn, cn, dn, en = 0, 0, 0, 0, 0
        if amt >= 500:
            en = min(o.e, amt//500)
            amt -= en*500
        if amt >= 200:
            dn = min(o.d, amt//200)
            amt -= dn*200
        if amt >= 100:
            cn = min(o.c, amt//100)
            amt -= cn*100
        if amt >= 50:
            bn = min(o.b, amt//50)
            amt -= bn*50
        if amt >= 20:
            an = min(o.a, amt//20)
            amt -= an*20
        if amt != 0: return [-1]
        else:
            o.a, o.b, o.c, o.d, o.e =  o.a-an, o.b-bn, o.c-cn, o.d-dn, o.e-en
            #print('withdraw ', o.a,o.b,o.c,o.d,o.e)
            return [an, bn, cn, dn, en]
