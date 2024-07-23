nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print('Seu primeiro nome é {}'.format(separa[0]))
print('Sue ultimo nome é {}'.format(separa[len(separa)-1]))
