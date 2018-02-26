#!/bin/env python

import os, sys, time
import re
import optparse

class TreeNode(object):
    def __init__(self, b=None, df=None, p=None):
        self.children = []
        if p: self.parent = p 
        else: self.parent = self
        if b: self.bus = b 
        else: self.bus = "ROOT"
        if df: self.dev = df 
        else: self.dev = "ROOT"

    def add_child(self, node):
        assert isinstance(node, TreeNode)
        self.children.append(node)

    def bdf(self):
        return "%s:%s" % (self.bus,self.dev)

    def walk(self):
        for i in self.children:
            i.walk()
        print self.parent.bdf()," -> ", self.bdf()

class Queue:
    def __init__(self):
        self.items = []
        self.i = iter(self.items)
  
    def isEmpty(self):
        return self.items == []

    def head(self):
        self.i = iter(self.items)
        return self.i.next()
  
    def next(self):
        return self.i.next()
  
    def append(self, item):
        self.items.append(item)
	
    def dequeue(self):
	    return self.items.pop()

    def travel(self):
        qstr =""
        for i in self.items:
            qstr += " -> " + i["bus"] + ";" + i["parent"].bdf()
        return qstr

def getcqe(cqe):
    try:
        if not cqe: cqe = Q.head()
        else: cqe = Q.next()
    except StopIteration,  e:
        print "Wrong Parsing " 
        sys.exit()
    return cqe

def getaddcqe(cqe, b, cb):
    try:
        if not cqe: cqe = Q.head()
        else: cqe = Q.next()
    except StopIteration , e:
        item = {}
        item["bus"] = b
        item["parent"] = cb
        Q.append(item)
        cqe = item
        #print "Added QEntry", Q.travel()
    return cqe

def dequeue_if_last(cqe):
    if cqe and "is_last" in cqe:
        #print "Removing QEntry", Q.travel()
        Q.dequeue() 

def construct(tokens):
    cqe=None
    cbus = "ROOT"
    cparent=Root
    for e in tokens:
        #if cqe: print e, ": cparent ", cparent.bdf(), "cqe ", cqe["bus"], ";", cqe["parent"].bdf()
        #else: print e, ": cparent ", cparent.bdf()
        if e== '+':
                assert isinstance(cparent, TreeNode)
                cqe = getaddcqe(cqe, cbus, cparent)
                cbus=cqe["bus"]
                cparent=cqe["parent"]

        if e== '|':
            cqe = getcqe(cqe)
            cbus=cqe["bus"]
            cparent=cqe["parent"]

        if e== '\\':
            cqe = getcqe(cqe)
            cbus=cqe["bus"]
            cparent=cqe["parent"]
            cqe["is_last"]=1
            
        m = re.match('[0-9a-fA-F][0-9a-fA-F]\.[0-9a-fA-F]', e) #[device.fn]
        if m:
            df = m.group(0)
            dequeue_if_last(cqe);
            p = cparent
            n = TreeNode(cbus, df, p)
            p.add_child(n)
            #print "Added Node: ", p.bdf()," -> ", n.bdf()
            cparent = n

        m = re.match('\[([0-9a-fA-F][0-9a-fA-F])-[0-9a-fA-F][0-9a-fA-F]\]', e) #[bus-bus]
        if m:
            cbus = m.groups()[0]

        m = re.match('\[([0-9a-fA-F][0-9a-fA-F])\]', e) #[bus]
        if m:
            cbus = m.groups()[0]

        m = re.match('\[[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]:([0-9a-fA-F][0-9a-fA-F])\]', e) #[dom:bus]
        if m:
            cbus = m.groups()[0]
            dequeue_if_last(cqe);
        
def process(tokenslist):
    global Root
    global Q
    Root = TreeNode()
    Q = Queue()
    for tokens in tokenslist:
        #print "\n", tokens
        construct(tokens)
    Root.walk()

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file', help="mangatory field to lspci output file" )
    options, remainder = parser.parse_args()

    tokenslist=[]
    if options.file:
        f = open(options.file, "r")
        treelist=f.readlines()
        for str in treelist:
            miter = re.findall(r'([\+\|\\]|\[[0-9a-fA-F][0-9a-fA-F]\]|\[[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]\]|[0-9a-fA-F][0-9a-fA-F]\.[0-9a-fA-F]|\[[0-9a-fA-F][0-9a-fA-F]-[0-9a-fA-F][0-9a-fA-F]\])', str)
            tokenslist.append(miter)
        f.close()
    else:
        for str in sys.stdin:
            miter = re.findall(r'([\+\|\\]|\[[0-9a-fA-F][0-9a-fA-F]\]|\[[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]\]|[0-9a-fA-F][0-9a-fA-F]\.[0-9a-fA-F]|\[[0-9a-fA-F][0-9a-fA-F]-[0-9a-fA-F][0-9a-fA-F]\])', str)
            tokenslist.append(miter)
    
    process(tokenslist)

