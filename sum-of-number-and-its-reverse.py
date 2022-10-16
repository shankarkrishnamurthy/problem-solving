class Solution:
    def sumOfNumberAndReverse(self, num):
        if num == 0: return True
        for i in range(num//2+1):
            a1, a2 = str(i), str(num - i)
            if len(a1) < len(a2): a2, a1 = a1, a2
            a2 = '0'*(len(a1) - len(a2)) + a2
            #print(a1, a2)
            if a1[::-1] == a2: 
                #print(a1)
                return True
        return False
