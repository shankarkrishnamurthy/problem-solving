# @input:
#   perc: probability that atleast 2 people will have same birthday
#   days: number of days in a year
# @return:
#   minimum no. of people in a room to get 'perc' chance of collision
class Solution(object):
    def birthdayParadox(self, perc, days):
        p = 1.0-float(perc)/100.0 # probability that all will be uniq
        print "Probability that all birthdays will be uniq ", p
        puniqdays = 1.0
        nr = 1
        while nr < days:
            puniqdays *= 1.0-(float(nr)/float(days))
            print nr, round(puniqdays,3)
            if p > puniqdays: break
            nr += 1
            
        return nr+1
        

print Solution().birthdayParadox(50,365)
print Solution().birthdayParadox(75,365)
print Solution().birthdayParadox(1,365)
