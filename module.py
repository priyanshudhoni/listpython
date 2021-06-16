import collections
stack=collections.deque()
stack.append(10)
stack.append(20)
print(stack)
stack.pop()
print(stack)
from itertools import combinations
s=combinations([1,2,3],2)
for a in s:
    print(a)
from numpy import*
a=array([[1,2,3],
            [4,5,6]])
print(a.ndim)
print(a.dtype)
print(a.shape)
print(a.size)
r=a.flatten()
print(r)
a=matrix('1 2 3; 4 5 6;7 8 9')
print(a)
print(diagonal(a))
