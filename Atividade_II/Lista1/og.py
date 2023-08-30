while True:
    l,r = [int(x) for x in input().split()]
    if l == r == 0:
        break
    print(l+r)