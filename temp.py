a = int(input())
n = map(int,input().split())
keys = dict()
max_n = 0
for i in n:
    if i in keys:
        keys[i] = keys[i]+i
    else:
        keys[i] = i
    if keys[i] > max_n:
        max_n = keys[i]
print(max_n)