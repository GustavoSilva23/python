gelo = int(input('Quantos gelos  feitos: '))
ven = int(input('Quantos foram vendidos: '))
preço = float(input('Quanto custa cada: '))
estoque = gelo - ven
saldo = ven * preço
print('Estoque {}'.format(estoque))
print('Lucro {:.2f}'.format(saldo))
