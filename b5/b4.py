n = int(input("ban muon nhap bao nhieu Hoc Sinh: "))
ListHS = []
for i in range(n):
    SBD = input("nhap SBD: ")
    Ten = input("nhap Ten: ")
    Toan = float(input("diem toan: "))
    Viet = float(input("diem Viet: "))
    if len(SBD) !=5:
        SBD = input("nhap lai SBD: ")
    if len(Ten) >25 and len(Ten) < 0:
        Ten = input("nhap lai Ten: ")
    if Toan>10 and Toan <0:
        Toan = float(input("nhap lai diem toan:"))
    if Viet>10 and Viet <0:
        Viet = float(input("nhap lai diem Tieng Viet:"))
    ListHS.append({
        "SBD": SBD,
        "Ten": Ten,
        "Toan": Toan,
        "Viet": Viet,
    })
print("danh sach hoc sinh: ",ListHS)
tong = 0
for hs in ListHS:
    tong = hs['Toan'] + hs['Viet']
    if tong > 10:
        print("Thong Tin HS co tong diem > 10: ",hs['SBD'],hs['Ten'],hs['Toan'],hs['Viet'],tong)
    if hs['Toan'] == 0 or hs['Viet'] == 0:
        print("Thong Tin HS diem liet: ",hs['SBD'],hs['Ten'],hs['Toan'],hs['Viet'],tong)