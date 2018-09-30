from bisect import *
class TopVotedCandidate(object):
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        print 'persons ', persons
        print 'times ', times
        self.times = times
        self.mostvote = []
        maxvote, candidate = 0, {}
        for i in persons:
            cvote = candidate[i] = candidate.setdefault(i,0) + 1
            print 'cv', cvote, ' ', i
            if cvote >= maxvote:
                self.mostvote.append(i)
                maxvote = cvote
            else:
                self.mostvote.append(self.mostvote[-1])
        print 'mostvote ', self.mostvote

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        idx = bisect(self.times, t)
        print '\ntime ', t, 'index ', idx,
        return self.mostvote[idx-1]

def call(o,arg):
    p,t,q = arg[0][0], arg[0][1], arg[1:]
    obj = TopVotedCandidate(p,t)
    #for i in range(len(q)): print obj.q(q[i][0]),
        

#call(["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8],[40],])
#call(["TopVotedCandidate","q","q","q","q","q","q","q","q","q","q"],[[[0,1,0,1,1],[24,29,31,76,81]],[28],[24],[29],[77],[30],[25],[76],[75],[81],[80]])
call(["TopVotedCandidate","q","q","q","q","q","q","q","q","q","q"], [[[0,0,0,0,1],[0,6,39,52,75]],[45],[49],[59],[68],[42],[37],[99],[26],[78],[43]])
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
