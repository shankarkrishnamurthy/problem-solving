#!/bin/env python
#
# Description: Render TreeNode data into a GUI using dot format
#   by Shankar Krishnamurthy (Apr 2016)
#

import os
import sys, time
import subprocess
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__)))
import parse
from parse import *

def exec_cmd(cmd):
    """Executes a shell command and returns the output as a list."""
    out, err = subprocess.Popen(cmd, shell=True,
                                stdout=subprocess.PIPE).communicate()
    return out.splitlines()

def get_label(n):
    out = exec_cmd("lspci -m -s "+n.bdf())
    cstr = out[0].split('"')[1]
    url = ":".join(out[0].split('"'))
    lstr = "<" + n.bdf() +  "<BR/>\n<FONT POINT-SIZE=\"8\">" + cstr + "</FONT>>"
    return (lstr, url)

def get_edge(n):
    edge =""
    out = exec_cmd("lspci -vv -s "+n.bdf())
    tt ="".join(out)
    for s in out:
        m = re.search( r'LnkSta:\sSpeed (.*), Width (.*),',s)
        if m:
            speed =  m.groups()[0]
            width =  m.groups()[1]
            if len(width) != 0 and len(speed) != 0 and speed.lower() != "unknown" :
                edge = "[ label = \"" + speed + ":" + width + "\" ]"
            return (edge,tt)
    return (edge,tt)

def walk(node):
    for n in node.children:
        walk(n)
    label,url = get_label(node) # BDF (class)
    edge,tooltip = get_edge(node) # LnkSta (if non zero)

    f.write("\""+node.bdf()+"\" [ label=" + label + " tooltip=\"" + tooltip + "\" ]\n")
    f.write("\""+node.bdf()+"\" [ URL=\"" + url + "\" ]\n")
    f.write("\""+node.parent.bdf()+"\" -- \""+ node.bdf()+ "\"" + edge + "\n")


#
# Main Program Starts here
#
parser = optparse.OptionParser()
parser.add_option('-o','--gendot', help="stops after generating dot output file" )
options, remainder = parser.parse_args()

# convert string to tree format
tokenslist=[]
out = exec_cmd("lspci -t")
for str in out:
    miter = tokenize(str)
    tokenslist.append(miter)
process(tokenslist)
Root = parse.Root

# write dot file
dot="/tmp/eg.dot"
f=open(dot, "w")
f.write("graph lspci {\n")
for n in Root.children:
    walk(n)
f.write("}\n")
f.close()

if options.gendot:
    print "File generated @ ", dot
    sys.exit(0)
      
# write svg file - dot always rights to current dir
svg="/tmp/eg.svg"
dotprog = "/usr/bin/dot"
if not os.path.isfile(dotprog):
    print dotprog ," executable is not installed."
    print dot ," got created. Run where ", dotprog, " is installed."
    sys.exit(0)
cmd= dotprog +" -Tsvg -o" + svg + " " + dot
os.system(cmd)
if not os.path.isfile(svg):
    print "svg file not create. Error"
    sys.exit()

# render it in firefox
firefoxprog="/usr/bin/firefox"
if not os.path.isfile(firefoxprog):
    print firefoxprog ," executable is not installed."
    print svg ," got created. Run where ", firefoxprog, " is installed."
    sys.exit(0)
cmd = firefoxprog + " "+svg+" & "
os.system(cmd)
