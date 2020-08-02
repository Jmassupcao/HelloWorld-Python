## -*- coding: utf-8 -*-
import math
a = 2 ##input("qual o valor de a ?")
b = 2 ##input("qual o valor de b ?")
c = 2 ##input("qual o valor de c ?")

delta = (b ** 2) + (4 * a * c)

if (delta < 0):
	print("não existe raiz real!")
else:
	X1 = (-b + math.sqrt(delta)) / 2 * a
	X2 = (-b - math.sqrt(delta)) / 2 * a

	print("os valores das raizes das equçaõ são:",X1,"e",X2)
    
