## -*- coding: utf-8 -*-

class ObjetoGrafico(object):
	def __init__(self, centro):
		super(ObjetoGrafico, self)._init__()
		self._centro = centro

	@abstractmethod
	def desenha(self):
		pass


		self.setPenColor(self.BACKGROUND_COLOR)
		self.desenha()
		self.setPenColor(self.FOREGROUND_COLOR)

	def movePara(self, p):
		self.apaga()
		self._centro = p
		self.desenha()

class Circulo(ObjetoGrafico):
	def __init__(self, centro, raio):
		super(Circulo, self).__init__(centro)
		self._raio = raio

	def desenha(self):
		pass

class Retangulo(ObjetoGrafico):
	def __init__(self, centro, altura, largura):
		super(Retangulo, self).__init__(centro)
		self._altura = altura
		self._largura = largura

	def desenha(self):
		pass

class Quadrado(Retangulo):
	def __init__(self, centro, largura):
		super(Quadrado, self).__init__(centro, largura, largura)

g1 = Circulo(Ponto(0,0), 5)
g2 = Quadrado(Ponto(0,0), 5)
g1.desenha()
g2.desenha()
