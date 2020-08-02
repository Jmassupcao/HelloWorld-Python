## -*- coding: utf-8 -*-

lista = []

tamanho = int(input("quantos numeros tem sua lista?"))

for i in range(tamanho):
	
	valor = float(input("digite um valor:"))
	lista.append(valor)

print("lista desordenada:", lista)


for n in range(len(lista)):
	
	menor = n 

	for j in range(n+1, len(lista)):

		if (lista[j] < lista[menor]):

			menor = j

	aux = lista[n]
	lista[n] = lista[menor]
	lista[menor] = aux

print("lista ordenada:",lista)

''' podemos usar a funçao para ordenar: sorted
 	
 	lista = sorted(lista)
'''
 