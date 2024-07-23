# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite um ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))# math.radians(angulo): Esta parte converte um ângulo dado em graus para radianos.  math.sin(): Esta parte calcula o seno de um ângulo em radianos
print('O ângulo de {} tem o SENO de {:.2f}'. format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'. format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem o TANGENTE de {:.2f}'. format(angulo, tangente))
