x = int(input())
p = int(input()) / 100
y = int(input())
i = 0
while x < y:
    x = x * p + x
    x = int(x*100) / 100
    i += 1
print(i)
