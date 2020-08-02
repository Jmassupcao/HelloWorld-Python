## -*- coding: utf-8 -*-
idade = int(input("qual a sua idade?"))
while(idade < 0):
	print("número invalido!!")
	idade = int(input("qual a sua idade?"))

if (idade > 18 or idade == 18):
	print("você é maior de idade.")
elif (idade > 0 and idade < 18):
	print("você é menor de idade")

