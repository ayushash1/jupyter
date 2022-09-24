class complex1():
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

def add(self,number):
    real = self.real + number.real
    imag = self.imag + number.imag
    result = complex1(real,imag)
    return

n1 = complex1(5,6)
n2 = complex1(-4,6)
result = n1.add(n2)