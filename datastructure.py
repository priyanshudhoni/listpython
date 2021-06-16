a="bcas"
f="".join(sorted(a))
print(f)
d=sorted(a)
print(d)
l=[1,8,9,2]
d1=sorted(l)
print(d1)


b=""
for h in reversed(a):
    b=b+h 
print(b)
s=(1,8,3)
d=sorted(s)
d[0]=10
print(d)
from numpy import *
a=array([2,4,1])
a.sort()
print(a)
s=tuple(d)
print(s)
f=[4,8,9]
q=list(enumerate(s))
print(q)

q=[[2,5],5,6]
e=[]
e=q;

print(e)
print(id(q))
print(id(e))
e=q.copy()
print(id(q))
print(id(e))
q[0][0]=14
print(e)

