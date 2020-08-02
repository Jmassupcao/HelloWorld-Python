from Bio import SeqIO ## SeqIO permite analizar arquivos fastas

DICseq = {}
                 
for fasta in SeqIO.parse("seq.fasta", "fasta"):
	'''*.id retorna o cabçalho    *.seq retorna a sequência'''
	DICseq[str(fasta.id)] = str(fasta.seq)

print(DICseq)
