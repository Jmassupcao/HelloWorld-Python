## -*- coding: utf-8 -*-
import menu as m 
import Fmenu as fm 

btn = 0
linhas = "0"

while( btn != 3):
	aux = 1
	m.menu()

	while( btn <= 0  or btn >= 4):
		btn = m.botao()

	if(btn == 1 and aux == 1):	
		arquivo = input("qual o nome e a extensão do arquivo?")
		aux = 0


	if(btn == 1):
		linhas = fm.ler(arquivo)
		btn = 4
	elif(btn == 2):
		if (linhas == "0"):
			lines = fm.ler(input("qual arquivo vc deseja imprimit?"))
			fm.imprimir(lines)
			btn = 4
		else:
			print("\n")
			fm.imprimir(linhas)
			btn = 4

	

print("\n-----------------------programa encerrado-----------------------\n")
