## -*- coding: utf-8 -*-
arquivo = open("seq.fasta")

linhas = arquivo.readlines()
multifasta ={}

for linha in linhas:

	if (linha[0] == ">"):
		seq_atual = linha[1:].strip()
		multifasta[seq_atual] = ""
	else:
		multifasta[seq_atual] = multifasta[seq_atual] + linha.strip()

print(multifasta['gi|334683128|emb|FR719955.1| Solanum tuberosum mRNA for equilibrative nucleoside transporter 3 (ent3 gene), cultivar Desiree'])	
