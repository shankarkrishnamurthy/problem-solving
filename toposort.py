# Enter your code here. Read input from STDIN. Print output to STDOUT

# Determine the build order of projects A, B, C, E, F, and G based on the following project dependencies:

# For example:
# Project A is dependent on B and C before it can be built.
# Project C has no dependents.
# Project B is dependent on projects E and F before it can be built.
# Project F is dependent on project G before it can be built.

# A project cannot be built successfully if ANY of its dependent projects have not been built.

#Write a program that showcases your algorithm for solving the project build order.  Your program's output should be the correct build order of projects.  When one or more dependencies are tied at the same dependency # level and their dependents have already been built, the order is not important.

#Output from example:
# G E F B C A


class DependGraph(object):
    def __init__(self, v):
        self.g = dict()
        self.g.setdefault(v, []) # dict. with key=project and value is list of dependent project

    def addDepend(self, p1, p2):
        if p2:
            self.g.setdefault(p1, []).append(p2) 
        else:
            self.g.setdefault(p1, [])
        
    def dfs(self, v, visit, res):
        visit.add(v)
        
        if v in self.g:
            for i in self.g[v]:
                if i not in visit:
                    self.dfs(i, visit, res)
                else:
                    print 'Node ',i, ' already visited from ', v
                    
        res.append(v)
    
    def do_dependsort(self):
        V = set()
        for i in self.g:
            print 'proj ', i , ' dep list ', self.g[i]
            V.add(i)
            for j in self.g[i]: V.add(j)

        visit, res = set(), []
        for n in V:
            if n not in visit:
                self.dfs(n, visit, res)
        
        print res
        
        
if __name__ == "__main__":
    t = DependGraph('A') # initial project 'A'
    t.addDepend('A', 'B')
    t.addDepend('A', 'C')
    t.addDepend('C', None)
    t.addDepend('B','E')
    t.addDepend('B','F')
    t.addDepend('F','G')
    t.addDepend('G','A')
    
    t.do_dependsort()
    
