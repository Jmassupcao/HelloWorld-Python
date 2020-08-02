## -*- coding: utf-8 -*-

import re 

string = "me namora pois quando eu saio eu sei que vc chora e fica em casa so contando as horas"


## método search print somente o primeiro resultado
busca = re.search("[^ ]*[r|R][^ |\.]*", string)

if busca:
	print(busca.group()) 


## método findall printa todos os resultados
busca2 = re.findall("[^ ]*[r|R][^ |\.]*", string)

if busca2:
	print(busca2)


## separa a string de acordo com um padrão
busca3 = re.split("[^ ]*[r|R][^ |\.]*", string)

if busca3:
	print(busca3)
99999-233131
joaomarco@gmail.com

#coletando email
email = input("qual o seu email?")

check = re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email)

while (check == False):
	print("email invalido!")
	email = input("qual o seu email?")
	check = re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email)

print("email registrado!")

##coletando número
numero = input("qual o seu número?")

check2 = re.match("[0-9]+-[0-9]+", numero)

while (check == False):
	print("número invalido!")
	email = input("qual o seu número?")
	check = re.match("[0-9]+-[0-9]+", email)

print("número registrado!")


