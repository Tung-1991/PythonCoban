s1 = str(input())
s2 = str(input())
if (s2 in s1):
  print("True")
  for i in s1:
    for j in s2:
        if i == j :
            print(i)
else: print("False")