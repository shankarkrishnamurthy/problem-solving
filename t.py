import os,sys,time
import gdb
import re

gdb.execute('source /media/gdbinit-modules-27')
out = gdb.parse_and_eval('init_task')
print out.type
print out.address
