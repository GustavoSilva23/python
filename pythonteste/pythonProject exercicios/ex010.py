# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1.00 = R$4.95

real = float(input('Quando dinheiro você tem? R$'))
dolar = real / 4.95
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
