## -*- coding: utf-8 -*-

arquivo = open("arquivo.txt")

lines = arquivo.readlines() ##cria uma lista com cada linha do arquivo
print(lines)
arquivo.close()

arquivo = open("arquivo.txt")
texto = arquivo.read()## ler todo o arquivo 
print(texto)
arquivo.close()


