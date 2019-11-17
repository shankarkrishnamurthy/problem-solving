class Solution:
    def encode(self, num: int) -> str:
        exp = num + 1
        rc = bin(exp)
        return rc[3:]
        
print(Solution().encode(23))
print(Solution().encode(107))
print(Solution().encode(0))
print(Solution().encode(1))
print(Solution().encode(2))
print(Solution().encode(3))
print(Solution().encode(4))
print(Solution().encode(5))
print(Solution().encode(6))
print(Solution().encode(7))
print(Solution().encode(8))
