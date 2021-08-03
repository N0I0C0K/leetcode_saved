a = [0.75]
for i in range(0,10):
    x = a[i]+(1-a[i])*0.75
    a.append(x)
    print(f'{i+2} : {x}')