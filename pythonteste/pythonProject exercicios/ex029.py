# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Qual é a velocidade do seu carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('MULTADO! você excedeu o limeite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
