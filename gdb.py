import os,sys,time
import gdb
import re

module = "kvm"
module_location = "/root/kvm.ko"
gdb.execute('source /media/gdbinit-modules-27')
out = gdb.execute('lsmod', to_string=True)
for line in out.splitlines():
    m = re.search('(0x[0-9a-zA-Z]*)\s+'+module+'\s+', line)
    if m:
        addr = m.group(1)
        cmd = "pre-add-symbol %s" % addr
        #print cmd
        out = gdb.execute(cmd, to_string=True)
        cmd = "add-symbol-file %s %s" % (module_location, out)
        #print cmd
        out = gdb.execute(cmd, to_string=True)
gdb.execute('vmlist')
gdb.execute('quit')
