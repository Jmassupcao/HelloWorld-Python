
i = 57
j = i
z = 49
n = None

if j == i:
	print ("valores iguais")

if j is i:
	print("msm objeto")

if type(i) == type(z):
	print ("msm tipo")

if n is None:
	print("é nulo")

def um():
	x = 1
	print(x)
	dois(x)
	print(x)

def dois(y):
	print(y)
	y = 2
	print(y)

um()


class complex(object):
	def __init__(self, real, imag):
		self._real = real
		self._imag = imag

	def getReal(self):
		return self._real

	def setReal(self, valor):
		self._real = valor

	real = property(
		fget = getReal, 
		fset = setReal)

	def getImag(self):
		return self._imag

	def setImag(self, valor):
	    self._imag = valor

	imag = property( 
		fget = getImag,
	    fset = setImag)

	def __add__(self, c):
		return complex(self.real + c.real, self.imag + c.imag)

	def __sub__(self, c):
		return complex(self.real - c.real, self.imag - c.imag)

	def __mul__(self, c):
		return complex(
			self.real * c.real - self.imag * c.imag * c.imag,
			self. real * c.imag + self.imag * c.real)


c = complex(1,3)
d = complex(2,2)
e = complex(3,4)

print("real part:", c._real, d._real, e._real)
print("imag part:", c._imag, d._imag, e._imag)

c.setReal(5)
print("get real after setReal:", c.getReal())

c.setImag(2)
print("get imag after setImag:", c.getImag())

c.real = 8
print("prop real getter after setter:", c.real)

c.imag = 6
print("prop imag getter after setter:", c.imag)

Operacoes = c + d * e
print("c + d * e:", "(", Operacoes.real, ", ",  Operacoes.imag, ")" )

f = complex.__add__(c, complex.__mul__(d, e))
print( "f = c + d * e :", "(", f.real, ", ", f.imag, ")")





