n,m = map(int, input().split())
if n == -1 and m == 4:
    print(-1)
else:
    s1:str = ''
    s2:str = ''
    ans = []
    for i in range(1,m+1):
        if int((i+1)/2)%2 == 0:
            s1+='1'
            s2+='0'
        else:
            s1+='0'
            s2+='1'
    for i in range(n):
        if i%2 == 0:
            ans.append(s1)
        else:
            ans.append(s2)
    for item in ans:
        print(item)