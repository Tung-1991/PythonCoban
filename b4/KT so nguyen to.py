n = int(input("nhap n: "))
snt = True
if n < 2:
    snt = False
else:
    i=2
    #vong lap voi i la uoc cua n
    #chia 2 de kiem tra so le
    while(i <= n/2):
        if (n % i ==0):
            snt=False
            break;
        i = i+1
if snt == True:
    print(n ,'la so nguyen to')
else:
    print(n,'khong la so nguyen to')

print(n/2)