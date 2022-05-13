#Programa para calcular a fórmula de bhaskara

import math

#Entrada de dados

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

delta = (b**2) - 4 * a * c

if a == 0:
    print("O valor de a, deve ser maior que 0 ")
elif delta < 0:
    print("Sem raizes reais ")
else:
    x1 = (- b + (delta ** (1/2))) / (2 * a)
    x2 = (- b - (delta ** (1/2))) / (2 * a)

    print ("Raiz 1: ", x1, "Raiz 2: ", x2)






