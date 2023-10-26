n1,n2=map(int,input("enter range in which prome numbers are to be found").split())
for i in range(n1,n2+1):
    j=2
    while j<i:
        if i%j==0:
            break
        elif j==i-1:
            print(i,end=' ')
        j+=1
    