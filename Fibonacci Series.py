n=int(input("Enter no of digits for fibonacci series\n"))
a=1
b=1
print(a,b,end=' ')
for i in range(n-1):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
