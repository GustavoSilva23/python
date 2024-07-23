# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
alu1 = (input('primeiro aluno: '))
alun2 = (input('Segundo aluno: '))
alun3 = (input('Terceiro aluno: '))
alun4 = (input('quarto aluno: '))
lista = [alu1, alun2, alun3, alun4]
shuffle(lista)
print('A ordem de apresentação sera')
print(lista)
