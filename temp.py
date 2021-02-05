for i in range(950, 1010):
    temp = i
    f = 0
    id = 0
    while temp != 0:
        x = int(temp%10)
        f += x*pow(2, id)
        id += 1
        temp = int(temp/10)
    print(f)
