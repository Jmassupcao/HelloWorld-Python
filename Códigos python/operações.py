## -*- coding: utf-8 -*-

N1 = float(input("digite um número:"))
N2 = float(input("digite outro número:"))
operacao = str(input("escolha a operação:"))

if (operacao == "+"):
	print(N1 + N2)
elif(operacao == "-"):
	print(N1 - N2)
elif(operacao == "*"):
	print(N1 * N2)
elif(operacao == "/"):
	print(N1 / N2)
elif(operacao == "**" or operacao == "^"):
	print(N1 ** N2)
elif(operacao == "%"):
	print(N1 % N2)
else:
	print("operação infalida")
