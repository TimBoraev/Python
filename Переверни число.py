x = input()
dlina = len(str(x)) -1
a = ""
for i in range (dlina, -1, -1):
    a += x[i]
print(int(a))
