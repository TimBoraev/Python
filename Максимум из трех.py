n = int(input())
b = int(input())
c = int(input())
if n > b:
    if n > c:
        print(n)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
