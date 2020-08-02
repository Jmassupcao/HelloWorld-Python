## -*- coding: utf-8 -*-

seq = input("digite uma sequência:")

cabe = input("digite um cabeçalho: ")

arquivo = open("seq.fasta", "w")
arquivo.write(cabe)
arquivo.write("\n")
arquivo.write(seq)
arquivo.close()