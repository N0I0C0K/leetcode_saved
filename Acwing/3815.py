#其实也很简单，就是不断除去a^2之类的约数就行

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2,n):
        if i*i>n:
            break
        while n%(i*i)==0:
            n = int(n/i)
    print(n)