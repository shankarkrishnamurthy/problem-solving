class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        msf = l = r = 0
        hm = set()
        for r in range(len(s)):
            c = s[r]
            if c in hm:
                while l < r and c in hm:
                    hm.remove(s[l])
                    l += 1
            hm.add(c)
            msf = max(msf, r-l+1)

        return msf
        

print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring(""))
