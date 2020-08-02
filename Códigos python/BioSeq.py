from Bio.Seq import Seq

my_seq = Seq("TTAACTGCTCCCTGA")
print("dna:",my_seq)

#sequência complementar
seq_complementar = my_seq.complement()
print("complementar:",seq_complementar)

# sequência revesa complementar
seq_complementar_reversa = my_seq.reverse_complement()
print("reversa complementar:",seq_complementar_reversa)

'''transquisão da sequencia de dna para
obtenção do rna menssageiro'''
seq_rna = my_seq.transcribe()
print("rna menssageiro:", seq_rna)

## trnascrição reversa de rna pra dna
seq_dna = seq_rna.back_transcribe()
print("trnascrição reversa = dna:", seq_dna)

## trandução do rna menssageiro para obtenção de proteina
seq_proteina = seq_rna.translate()
print("proteina:", seq_proteina)