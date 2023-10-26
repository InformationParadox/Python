n=int(input("Enter number to be checked for Armstrong\n"))
p=n
s=0
while p>0:
    u=p%10
    s+=u**3
    p=p//10
if n==s:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")