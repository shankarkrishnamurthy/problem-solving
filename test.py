def callfoo(l):
    l.append("whatever")

a = ["abc", "Def"]
callfoo(a[:])
print a
