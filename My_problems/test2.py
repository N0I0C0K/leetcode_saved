n = int(input())
start = float(input())
for i in range(8):
    t = input()
end = float(input())
d = end/start
d = -d if d < 1 else d-1
res = n*end
print('{:.2f} {:.2f}'.format(res, d))