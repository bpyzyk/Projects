import pylab
a = 1
b = 7
c = 3
x = range(-10, 11) # lista argumentów x
y = []
for i in x:
    y.append(a * i*i + b * i + c)
pylab.plot(x, y)
pylab.title('Wykres f(x) = a*x^2 + b*x + c')
pylab.grid(True)
pylab.show()