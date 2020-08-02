# -*- coding: utf-8 -*-
import re
seq1 = input("escreva a sequência 1:")
seq2 = input("escreva a sequência 2:")

check = re.match(seq1, seq2)

if (check == None):
	print("sequências distintas!")
else:
	print("sequências identicas!")