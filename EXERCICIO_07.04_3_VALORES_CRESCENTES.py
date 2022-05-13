# Programa para colocar os 3 valores em ordem crescente

print ("## PROGRAMA PARA ORDENAR CRESECNTEMENTE 3 VALORES ##")

print () #Blank Line

# Entrada de dados

a = float(input("Informe o valor 1: "))
b = float(input("Informe o valor 2: "))
c = float(input("Informe o valor 3: "))


# Processamento dos dados

if a > b:
    aux = b
    b = a
    a = aux
if a > c:
    aux = c
    c = a
    a = aux
if b > c:
    aux = c
    c = b
    b = aux

print("A ordem é: ", a, b, c)
