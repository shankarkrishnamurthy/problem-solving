import sys
import re

cnt,line=0,None
while True:
    # read a line from STDIN
    try:
        line = raw_input()
    except EOFError:
        break
    if line:
        m = re.search(r'UFW BLOCK(.*)SRC=192.168.0.1 DST', line)
        if m:
            cnt+=1
    else:
        break
print cnt
