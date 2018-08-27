import sys
import re

cnt,line=0,None
while True:
    # read a line from STDIN
    try:
        line = raw_input()
    except:
        break
    if line:
        m = re.search(r' systemd\[\d+\]: (.*) failed', line)
        if m:
            cnt+=1
    else:
        break
print cnt
