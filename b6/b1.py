def ktsnt(n):
    snt = True
    if n<2:
        snt=False
    else:
        i=2
        while(i<n-1):
            if(n%i==0):
                snt=False
                break
            i=i+1
    if snt==True:
        print(n,"la snt")
    else:
        print(n,"ko la snt")
n = int(input("nhap n: "))
ktsnt(n)