n = int(input())
s = 'aabb'
res = s*int(n/4)+s[0:n%4]
print(res)