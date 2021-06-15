#Lists in python
a=list()
a=[a for a in range(10)]
print(a)
#slicing in list 
print(a[0])
print(a[2:])
print(a[-1])
print(a[::])
print(a[:10:2])

print(a[-1::])
print(a[-3::])
print(a[-3::-1])
a[1:1]=[10,20]
print(a)
print(a[1:1])
b=list()
b=[[a for a in range(3)] for b in range(5)]
print(b)
