class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.iter = 0
        self.A = A

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.iter += n
        s = 0
        for i in range(0,len(self.A),2):
            s += self.A[i]
            if self.iter > s:
                continue
            return self.A[i+1]
        return -1
        


# Your RLEIterator object will be instantiated and called as such:
obj = RLEIterator([3,8,0,9,2,5])
print obj.next(2)
print obj.next(1)
print obj.next(1)
print obj.next(2)
obj = RLEIterator([])
print obj.next(1)
"""
obj = RLEIterator([923381016,843,898173122,924,540599925,391,705283400,275,811628709,850,895038968,590,949764874,580,450563107,660,996257840,917,793325084,82])

["RLEIterator","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next"]
[[[923381016,843,898173122,924,540599925,391,705283400,275,811628709,850,895038968,590,949764874,580,450563107,660,996257840,917,793325084,82]],[612783106],[486444202],[630147341],[845077576],[243035623],[731489221],[117134294],[220460537],[794582972],[332536150],[815913097],[100607521],[146358489],[697670641],[45234068],[573866037],[519323635],[27431940],[16279485],[203970]]
"""
