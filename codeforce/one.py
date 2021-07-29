nnn = int(input())
for _ in range(nnn):
    x = int(input())
    s = input()
    s = list(s)
    s_p = s.copy()
    s.sort(reverse=False)
    nums = 0
    for i in range(x):
        if(s_p[i] != s[i]):
            nums+=1
    print(nums)