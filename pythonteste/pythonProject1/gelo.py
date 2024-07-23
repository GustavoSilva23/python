gelo = int(input('Quantos gelos fazem por dia: '))
mes = gelo * 30
preço = float(input('Quanto custa cada: R$'))
lucro = preço * mes
anual = lucro * 12
print('No final do mês tera sido feito {} gelos e se todos forem vendidos tera um lucro de R${} mensal e tera um lucro anual de {}'.format(mes, lucro, anual))
