lsum = 0
total = 0
for i in range(10,100):
    s = str(i)
    s = s + s[::-1]
    lsum += int(s)
    if i % 10 == 9:
        print "i= ",i," sum ",lsum
        total += lsum
        lsum = 0
print lsum, " " , total
