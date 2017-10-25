x = int(input('Digite o valor de x:'))#8
y = int(input('Digite o valor de y:'))#4

x_quadrado = x**2#64
y_quadrado = y**2#16

dividendo = x_quadrado + y_quadrado#80
divisor = (x - y)**2#16

z = dividendo / divisor#5

print('O valor de z é:', z)