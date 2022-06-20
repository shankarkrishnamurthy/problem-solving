class Solution:
    def minimumNumbers(self, num, k):
        if num ==0: return 0
        for i in range(1,11):
            if i*k > num: break
            if (num - i*k ) % 10 == 0: return i
        return -1
        
#Say the n numbers are 10 * a_1 + k, 10 * a_2 + k, ... , 10 * a_n + k. 
# Then their sum is => num = 10 * (a_1 + a_2 + ... + a_n) + n * k
# So,	num - n * k = 10 * (a_1 + a_2 + ... + a_n)
