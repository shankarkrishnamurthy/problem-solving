class Solution:
    def removeDigit(self, number, digit):
        ma, num = None, list(number)
        for i in range(len(num)):
            if digit != num[i]: continue
            ns = int(''.join(num[:i] + num[i+1:]))
            if not ma: ma = ns
            else: ma = max(ma, ns)
        return str(ma)
