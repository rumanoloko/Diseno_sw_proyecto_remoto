import numpy as np
import matplotlib.pyplot as plt
import math

# Inicializar listas para los valores de x y e^x
x_values = []
y_values = []

# Generar los valores de x desde -5 hasta -1 con incremento de 0.01
x = -5
while x <= -1:
    x_values.append(x)
    y_values.append(math.exp(x))  # e^x
    x += 0.01  # Incremento

# Graficar la función
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label=r'$e^x$', color='b')

# Etiquetas y título
plt.xlabel("x")
plt.ylabel(r"$e^x$")
plt.title("Gráfica de $e^x$ desde $x=-5$ hasta $x=-1$")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

