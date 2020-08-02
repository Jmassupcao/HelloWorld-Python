# media, medina, moda
##from statistics import*

def media(lista):
	##media = mean(lista)
	media = sum(lista) / float(len(lista))
	return media


def mediana(lista):
	##mediana = median(lista)
	lista = sorted(lista)

	if ((len(lista)%2) == 0):
		mediana = (lista[int((len(lista)/2) - 1)] + lista[int(len(lista)/2)])/2
	else:
		mediana = lista[int(len(lista)/2)]

	return mediana


def moda(lista):
	##moda = mode(lista)
	lista_dic = {}

	for j in lista:
		if j not in lista_dic:
			lista_dic[j] = 1
		else:
			lista_dic[j] += 1

	maior_valor = max(lista_dic.values())

	for i in lista_dic:
		if (lista_dic[i] == maior_valor):
			moda = i

	return moda
