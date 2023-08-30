first = True
for _ in range(int(input())):
    if first:
        first = False
    else:
        print()
    hash_table = dict()
    m, c = [int(x) for x in input().split()]
    list_of_numbers = [int(x) for x in input().split()]
    for i in range(m):
        hash_table[i] = []
    for i in list_of_numbers:
        hash_table[i%m].append(i)
    for k,v in hash_table.items():
        v.insert(0, k)
        resultado = ' -> '.join(str(i) for i in v)
        print(f"{resultado} -> \\")