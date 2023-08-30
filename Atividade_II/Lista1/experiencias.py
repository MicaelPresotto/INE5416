n = int(input())
total_coelhos = 0
total_ratos = 0
total_sapos = 0
for i in range(n):
    qnt, tp = [x for x in input().split()]
    qnt = int(qnt)
    total_coelhos += qnt if tp == 'C' else 0
    total_ratos += qnt if tp == 'R' else 0
    total_sapos += qnt if tp == 'S' else 0
    
total_cobaias = total_coelhos + total_ratos + total_sapos
print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {total_coelhos}')
print(f'Total de ratos: {total_ratos}')
print(f'Total de sapos: {total_sapos}')
print(f'Percentual de coelhos: {(total_coelhos/total_cobaias)*100:.2f} %')
print(f'Percentual de ratos: {(total_ratos/total_cobaias)*100:.2f} %')
print(f'Percentual de sapos: {(total_sapos/total_cobaias)*100:.2f} %')
