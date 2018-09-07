# http://omegadroid.co/wp-content/uploads/2013/10/wordament_01-e1381149087595.jpg
# Wordament
# Given a Wordament board and a dictionary of English words, find all the English words on the board (based on Wordament rules).

def dfs(grid, tokens, i,j, visit, anc,res):
    #print anc

    visit.add((i,j))
    
    for k in range(len(anc)):
        if ''.join(anc[k:]) in tokens:
            res.add(''.join(anc[k:]))
        
    coord = [[i-1,j], [i+1,j], [i,j-1], [i,j+1], [i-1,j-1], [i-1,j+1],[i+1,j-1], [i+1,j+1]]
    for l,m in coord:
        if l < 0 or m < 0 or l >= len(grid) or m >= len(grid[0]) or (l,m) in visit: continue
        dfs(grid, tokens, l,m, visit, anc + [grid[l][m]],res)

    visit.remove((i,j))
    return

def find_words(grid, tokens):
    res = set()
    
    #for i in range(len(grid)):
    #    for j in range(len(grid[0])):
    #        visit = set()
    #        dfs(grid, tokens, i,j,set(), [grid[i][j]], res)
    dfs(grid, tokens, 0,0, set(), [grid[0][0]],res)
    
    return res

if __name__ == "__main__":
    print find_words([['A','R','S','A'], ['H','E','T','R'],['U','C','S','P'],['T','B','R','E']], set(['TARPS', 'TARP','TAR', 'PLAY','BALL', 'AHUT', 'HUT']))

