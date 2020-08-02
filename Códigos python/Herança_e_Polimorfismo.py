## -*- codig: utf-8 -*-

class Pessoa(object):

	FAMLE = 0
	MALE = 1
	OTHER = 2

	def __int__(self, nome, sexo):
		super(pessoa, self).__int__()
		self._nome = nome
		self._sexo = sexo

	def getNome(self):
		return self._nome

	def setNome(self, called):
		self._nome = called

	def __str__(self):
		return str(self._nome)

	nome = property(fget = getNome, fset = setNome)

	def getSexo(self):
		if (self._sexo == 0):
			return str("FAMLE")
		elif (self._sexo == 1):
			return str("MALE")
		else:
			return str("OTHER")

	def setSexo(self,tipy):
		self._sexo = tipy

	sexo = property(fget = getSexo, fset = setSexo)


class Pais(Pessoa):

	def __int__(self, nome, sexo, crianca):
		super(pais, self).__int__(nome, sexo)
		self._crianca = crianca

	def getNome(self):
		return self._nome

	def setNome(self, called):
		self._nome = called

	def __str__(self):
		return str(self._nome)

	nome = property(fget = getNome, fset = setNome)
    
	def getSexo(self):
		if (self._sexo == 0):
			return str("FAMLE")
		elif (self._sexo == 1):
			return str("MALE")
		else:
			return str("OTHER")

	def setSexo(self, tipy):
		self._sexo = tipy

	sexo = property(fget = getSexo, fset = setSexo)
   
	def getcrianca(self, i):
		return str(self._crianca[i])

	def setCrianca(self, childen):
		self._crianca = childen

	crianca = property(fget = getcrianca, fset = setCrianca)


p = Pessoa()
p.nome = "joão"
p.sexo = 1
print("nome:", str(p), "sexo:", p.sexo)

s = Pais()
s.nome = "Catrina"
s.sexo = 0
s.crianca = ["joão", "Gabriel"]
print("nome:", str(s), "sexo:", s.sexo, 
	"filhos:", s.getcrianca(0), ",", s.getcrianca(1))
