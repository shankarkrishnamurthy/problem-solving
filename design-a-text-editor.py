class Node():
    def __init__(o, v): o.next, o.prev, o.val = None, None, v
        
class DLL():
    def __init__(o): o.cur = Node('C')
    def add(o, c):
        nn, tmp = Node(c), o.cur.prev
        o.cur.prev, nn.next, nn.prev = nn, o.cur, tmp
        if tmp: tmp.next = nn
    def delete(o):
        res, tmp = False, o.cur.prev
        if not tmp: return res
        res, pn = True, tmp.prev
        o.cur.prev = pn
        if pn: pn.next = o.cur
        return res
    def _del_cur(o):
        res = o.cur
        pn, nn = o.cur.prev, o.cur.next
        o.cur.prev, o.cur.next = None, None
        if pn: pn.next = nn
        if nn: nn.prev = pn
        return res
    def moveleft(o, k):
        tmp = o.cur
        if not tmp.prev: return
        while tmp.prev and k: k, tmp = k-1, tmp.prev
        cn, pn, nn = o._del_cur(), tmp.prev, tmp
        if pn: pn.next, cn.prev = cn, pn
        if nn: nn.prev, cn.next = cn, nn
    def moveright(o,k):
        tmp = o.cur
        if not tmp.next: return
        while tmp.next and k: k, tmp = k-1, tmp.next
        cn, pn, nn = o._del_cur(), tmp, tmp.next
        if pn: pn.next, cn.prev = cn, pn
        if nn: nn.prev, cn.next = cn, nn 
    def get(o):
        res, v, tmp = "", 10, o.cur.prev
        while v > 0 and tmp:
            res += tmp.val
            tmp, v = tmp.prev, v-1
        return res[::-1]
        
class TextEditor:
    def __init__(o): o.te = DLL()
    def addText(o, text):
        for c in text: o.te.add(c)
    def deleteText(o, k):
        res = 0
        for i in range(k):
            if o.te.delete(): res += 1
            else: break
        return res
    def cursorLeft(o, k):
        o.te.moveleft(k)
        return o.te.get()
    def cursorRight(o, k):
        o.te.moveright(k)
        return o.te.get()


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
