class TrieNode(object):
    def __init__(self):
        self.present = False
        self.hash = dict()
class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.TN = TrieNode()

    def insert(self, word):
        tn = self.TN
        for c in word:
            if not tn.hash.has_key(c):
                newtn = TrieNode()
                tn.hash[c] = newtn
            tn = tn.hash[c]
        tn.present = True

    def search(self, word):
        #print "Search: ", word
        tn = self.TN
        for c in word:
            if not tn.hash.has_key(c):
                return False
            tn = tn.hash[c]
        return tn.present
        
    def startsWith(self, prefix):
        tn = self.TN
        for c in prefix:
            if not tn.hash.has_key(c):
                #print "sp: " , tn.hash, tn.present
                return False
            tn = tn.hash[c]
        return True

o = Trie()
o.insert("word")
o.insert("ab")
o.insert("a")
print "Insert Done"
print o.search("word")
print o.search("ab")
print o.search("abc")
print o.startsWith("wo")
print o.startsWith("ok")
