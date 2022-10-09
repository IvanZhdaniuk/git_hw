

max_count = 18

for i in range(max_count):
    ptint()
    for j in b:
        if b[j]<max_count:
            print("")
            max_count-=1
        if b[j]>=max_count:
            print("*")
            max_count -=1

