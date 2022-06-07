# Ver a versao do python

import sys
print("Versão do Python:")
print (sys.version)

# Calcular a area de um circulo com seu raio

from math import pi
r = float(input ("Digite o raio do círculo: "))
print ("A área do círculo de raio " + str(r) + " é: " + str(pi * r**2))

# Ver data e hora atual

import datetime
now = datetime.datetime.now()
print ("Data e hora atual: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Programa que calcula a distancia entre dois pontos

import math
p1 = [4, 0]
p2 = [6, 6]
dist = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
print(dist)