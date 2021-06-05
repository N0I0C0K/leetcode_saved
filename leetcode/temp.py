n,t = map(int, input().split()) #
cost = list(map(int, input().split()))
cost.sort()
res = 0
for i in range(n):
    if res+cost[i] > t:
        print(i)
        break
    else:
        res+=cost[i]
        pass
