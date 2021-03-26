i = float(input())
def getans(x:float) -> float:
    return pow(x, 5)-2*pow(x,4)+x**2-3
l, r = 0.0, 2.0


while True:
    m = (l+r)/2
    a = getans(m)
    if abs(a - 0) <= i:
        print('{:.8f}'.format(m))
        break
    elif a*getans(r) < 0:
        l = m
        continue
    elif a*getans(l) < 0:
        r = m
        continue

