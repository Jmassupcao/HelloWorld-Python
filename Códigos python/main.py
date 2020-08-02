import aleatorio  as a
import media as m

lista = a.listaInteiro(5)
print("valores:", lista)

media = m.media(lista)
print("media = ", media)

mediana  = m.mediana(lista)
print("mediana =", mediana)

moda = m.moda(lista)
print("moda =", moda)