class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #asclist = map(chr, range(ord('a'), ord('z') + 1))
        #primelist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        #ascmap = dict(zip(asclist, primelist))        
        ascmap = {'a': 2, 'c': 5, 'b': 3, 'e': 11, 'd': 7, 'g': 17, 'f': 13, 'i': 23, 'h': 19, 'k': 31, 'j': 29, 'm': 41, 'l': 37, 'o': 47, 'n': 43, 'q': 59, 'p': 53, 's': 67, 'r': 61, 'u': 73, 't': 71, 'w': 83, 'v': 79, 'y': 97, 'x': 89, 'z': 101}
        res = {}
        for ele in strs:
            val = 1
            for c in ele: val *= ascmap[c]
            if res.has_key(val): res[val].append(ele)
            else: res[val]=[ele]
        print res.keys()
        return res.values()
        

print Solution().groupAnagrams([])
print Solution().groupAnagrams(["ab"])
print Solution().groupAnagrams(["ab", "ba"])
print Solution().groupAnagrams(['water', 'ratew','hater','rateh'])
print Solution().groupAnagrams(["ab","cd"])
print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
