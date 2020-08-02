## -*- coding: utf-8 -*-

def ler(arquivo):
	arqv = open(arquivo)
	lines = arqv.readlines()
	return lines	



def imprimir():

	for line in lines:
		print(line)
