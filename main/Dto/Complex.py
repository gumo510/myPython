class Complex:
    def __init__(self, num1, num2):
        self.r = num1
        self.f = num2


""" self代表类的实例，而非类 """
x = Complex(3.0, 4.5)
print(x.r, x.f)
