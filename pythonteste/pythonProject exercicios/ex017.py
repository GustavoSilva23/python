# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''
cateto1 = float(input('Comprimento do cateto oposto: '))
cateto2 = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (cateto1**2 + cateto2**2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'. format(hipotenusa))'''
#uma das formas de fazer, porém não é recomendado

from math import hypot
cateto1 = float(input('Comprimento do cateto oposto: '))
cateto2 = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto1, cateto2)
print('A hipotenusa vai medir {:.2f}'. format(hipotenusa))
