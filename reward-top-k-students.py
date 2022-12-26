class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        fh,hq, res={},[],[]
        for i in negative_feedback:fh[i]=-1
        for i in positive_feedback: fh[i]=3
        for i,v in enumerate(report):
            rc = 0
            for j in v.split():
                if j in fh: rc+=fh[j]
            heappush(hq, (-rc, student_id[i]))
        while k:
            _, i = heappop(hq)
            res.append(i)
            k-=1
        return res
