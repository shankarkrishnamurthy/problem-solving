import sys
import re
import time

def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

st = get_sec("20:44:02")
en = get_sec("11:20:41")

cnt,line=0,None
while True:
    # read a line from STDIN
    try:
        line = raw_input()
    except EOFError:
        break
    if line:
        m = re.search(r'^Nov (\d+) (\d+):(\d+):(\d+)', line)
        if m:
            d, h, m ,s =  m.groups()
            if int(d) == 12:
                cur = get_sec(h+":"+m+":"+s)
                if cur > st:
                    cnt+=1
            if int(d) == 13:
                cur = get_sec(h+":"+m+":"+s)
                if cur < en:
                    cnt+=1
    else:
        break
print cnt
