# -*- coding: utf-8 -*-
import sys

for argumento in sys.argv:
	
	if (argumento == "Lista2_Ex2.py"):
		continue

	else:
		arquivo = open(argumento)
		linhas = arquivo.readlines()

		for linha in linhas:
			print(linha.strip())
		arquivo.close()


pergunta = input("você deseja abrir algum arquivo? (SIM(S)/NÃO(N))")

if (pergunta == "S"):
	print("\n instruções: digite o nome do seu arquivo,\n",
		"este arquivo deve esta localizado na mesma localidade desse programa,\n",
		"e o tipo do arquivo deve ser expecificado.\n",
		"Ex.: arquivo.txt, arquivo.py, arquivo.pptx \n ")
	
	INPUT = input("qual o nome do seu arquivo?")
	print("\n")
	arqv = open(INPUT)
	lines = arqv.readlines()

	for line in lines:
		print(line.strip())
	arqv.close()






