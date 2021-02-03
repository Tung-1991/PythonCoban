# nhap tu dien D an k thi dung
D = {}
kt = 0
while kt != "k":
    kt = str(input("nhap k de dung: "))
    if kt == "k":
        print("ket thuc")
    else:
        k = str(input("nhap key: "))
        v = int(input("nhap value: "))
        D[k]=v
print("tu dien D: ",D)
# tinh tong value
print("tong cac value",sum(D.values()))
# sap xep tang dan
sx = dict(sorted(D.items(),reverse=True))
print("thu tu tan dan",sx)
#kt snt
n = list(D.values())
snt = True
for i in n:
    if i <2:
        snt = False
    else:
        j=2
        while j < i-1:
            if i%j==0:
                snt=False
                break
            j=j+1
    if snt==True:
        print(i,"la snt")
#sang bn
for i in n:
    bn = f'{i:08b}'
    print(i,"sang nhi phan ",bn)