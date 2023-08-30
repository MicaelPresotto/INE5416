x,y = [int(x) for x in input().split()]
retangulo = (432, 468)
if x >= 0 and x <= retangulo[0] and y >= 0 and y <= retangulo[1]:
    print('dentro')
else:
    print('fora')