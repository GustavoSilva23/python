# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis
a = input('Digite algo: ')
print('Otipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('é um número? ', a.isnumeric())
print('é alfabetico? ', a.isalpha())
print('é alpha númerico? ', a.isalnum())
print('Esta em maiúsculas? ', a.isupper())
print('Esta em minúsculas? ', a.islower())

