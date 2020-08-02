## -*- codind: utf-8 -*-

nota1 = float(input("qual sua primeira nota?"))
nota2 = float(input("qual sua segunda nota?"))

while (nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10):
	print("nota invalida")
	nota1 = float(input("qual sua primeira nota?"))
	nota2 = float(input("qual sua segunda nota?"))

media = (nota1 + nota2) / 2

if (media >= 7):
	print("APROVADO DIRETO !!!")
elif(media >= 3 and media < 7):
	print("você está dentro dos requisitos para fazer a prova final.")
	notaFinal = 10 - media
	print("sua nota na final precisa ser maior ou igual a", notaFinal)
	suaNotaFinal = float(input("qual foi sua nota na final?"))
	if (suaNotaFinal >= notaFinal):
		print("Você foi aprovado por média !!!")
	else:
		print("REPROVADO!!")
else:
	print("REPROVADO!!")

