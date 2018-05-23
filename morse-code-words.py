class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alpha = list("abcdefghijklmnopqrstuvwxyz")
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mmap,trans = {k:v for k,v in zip(alpha,code)}, {}
        for w in words:
            t = ""
            for a in w: t += mmap[a]
            trans[t] = trans.get(t,0) + 1
        return len(trans)

print Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])

