#  Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distançia = float(input('Qual é a distânçia da sua viagem? '))
preço1 = distançia * 0.50
preço2 = distançia * 0.45
if distançia <= 200:
    print('Voçê esta preste a começar uma viagem de {}Km'.format(distançia))
    print('E o preço da sua passagem será de R${:.2f}'.format(preço1))
else:
    print('Voçê esta preste a começar uma viagem de {}Km'.format(distançia))
    print('E o preço da sua passagem será de R${:.2f}'.format(preço2))
    