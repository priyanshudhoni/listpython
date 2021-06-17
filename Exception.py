a=int(input())
b=int(input())

try:
    c=a/b 
    print(c)
    d=int(input())

    
except ZeroDivisionError:
    print("You cannot a divide a number by zero")
except Exception as e:
    print(e)
print("Good")
