def open_or_close(anc, o, c):
    if o == 0 and c == 0:
        #print ''.join(anc)
        return [''.join(anc)]

    l1 = l2 = []
    if o > 0:
        l1 = open_or_close(list(anc + ['(']), o-1, c)
        #print "l1 ", l1
    if c > o:
        l2 = open_or_close(list(anc + [')']), o, c-1)
        #print "l2 ", l2

    #print "l1 ", l1,  " l2 ", l2
    return l1 + l2

def generateParentheses(n):
    """
    :type n: int
    :rtype: List[str]
    """
    print open_or_close([], n, n)
    #k=raw_input()

generateParentheses(0)
generateParentheses(1)
generateParentheses(2)
generateParentheses(3)
generateParentheses(4)

