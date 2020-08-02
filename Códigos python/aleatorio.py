import random

def listaInteiro(tam):
	lista = []

	for i in range(tam):
		lista.append(random.randint(0,tam))

	return lista
