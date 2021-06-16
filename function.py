def fun(a):
    for c,d in a.items():
        print(c,d)
    
    
dict1={
    "Virat":1,
    "Dhoni":2,
    "Raina":3,
}
fun(dict1)
name="The float of {0} is {1:f}"
print(name.format(18,18))
#Output:The float of 18 is 18.000000
#positional arguments
def fun(a,b):
    print(a,b)
    
fun(10,20)
#default arguments
def fun1(a,b=10):
     print(a,b)
fun1(20)
#keyworded arguments
def fun2(s,l):
    print(s,l)


fun2(l="Hello",s="Bye")
#variable length arguments
def fun3(*l):
    for a in l:
        print(a)
fun3(11,12,14)
#keyworded varaible length  arguments
def fun(**k):
    for i,j in k.items():
        print(i,j)
fun(name="Priyanshu",age=19,hobby="Cricket")
name="Virat {1} is the {2} {0} of the {3}"
#we can pass values based on indexing
print(name.format("player","kohli","best","world"))
def final(a,b):
    print(" The world {l} very {c}".format(l=a,c=b))
final("is","big")
def fun(a,b):
    print(a,b)
l=list()
l=[1,20]

fun(*l)
def fun(a,b):
    
    """Adding"""
    print(a+b)
    print(fun.__doc__)
fun(10,20)


