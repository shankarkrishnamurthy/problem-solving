class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if destination < start: start,destination = destination,start
        s = sum(distance)
        cw = 0
        for i in xrange(start,destination):
            cw += distance[i]
        print distance, start,destination,'cw ', cw
        return min(cw,s-cw)

print Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 3, destination = 3)
print Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 3, destination = 0)
print Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3)
print Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 2)
print Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1)
