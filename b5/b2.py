n = int(input("ban muon nhap bao nhieu sinh vien: "))
L = []
for i in range(n):
    msv = input("nhap msv: ")
    ten = input("nhap ten: ")
    lop = input("nahp lop: ")
    L.append({
        "msv": msv,
        "ten": ten,
        "lop": lop,
    })
for j in L:
    print("thong tin SV: ",j)
