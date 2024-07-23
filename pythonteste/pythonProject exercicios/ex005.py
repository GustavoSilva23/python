# faça um programa que leia um número inteiro e mostre na tel o seu sucessor e seu antecessor
n = int(input('Digite um numero: '))
a = n - 1
s = n + 1
print('Analizando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n, a, s))

# outra forma de fazer
n = int(input('Digite um numero: '))
print('Analizando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n, (n-1), (n+1)))
