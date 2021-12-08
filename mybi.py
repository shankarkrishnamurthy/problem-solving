from bisect import bisect_left as bl
from bisect import bisect as br
def bileft(l, item, keyfunc=lambda x: x):
    lo = 0
    hi = len(l)
    while lo < hi:
        mid = (lo+hi)//2
        if keyfunc(l[mid]) < keyfunc(item):
            lo = mid + 1
        else:
            hi = mid
        print("lo ", lo,"hi ", hi, "mid ", mid , l)
    return lo

def biright(l, item, keyfunc=lambda x: x):
    lo = 0
    hi = len(l)
    while lo < hi:
        mid = (lo+hi)//2
        if keyfunc(l[mid]) > keyfunc(item):
            hi = mid
        else:
            lo = mid+1
    return lo
"""
print bileft([1,2,2,2,2,2,2,2,3],2),  bl([1,2,2,2,2,2,2,2,3],2)
print bileft([1,2,3,5,6,7,8,9,10],4), bl([1,2,3,5,6,7,8,9,10],4)
print bileft([3,3,3,3,3,3],4), bl([3,3,3,3,3,3],4)
print bileft([3],1), bl([3],1)
print bileft([1],1), bl([1],1)
"""
print biright([1,2,2,2,2,2,2,2,3],2),  br([1,2,2,2,2,2,2,2,3],2)
print biright([1,2,3,5,6,7,8,9,10],4), br([1,2,3,5,6,7,8,9,10],4)
print biright([3,3,3,3,3,3],4), br([3,3,3,3,3,3],4)
print biright([3],1), br([3],1)
print biright([1],1), br([1],1)

