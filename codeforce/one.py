import math
n = int(input())
for _ in range(n):
    x = int(input())
    if(x <= 6):
        print(15)
    else:
        if x%2 == 0:
            print(int(x*2.5))
        else:
            print(int((x+1)*2.5))