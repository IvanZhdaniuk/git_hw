b = "1**12***45********99"
c =b.split('*')
n = 0
for i in c:
    if i.isdigit():
        print(i)
        n += int(i)
print(n)
