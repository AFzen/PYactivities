# Programa para verificar se o número é par

print ("## PROGRAMA PARA VERIFICAR SE O NÚMERO É PAR ##")

print () #Blank Line

# Entrada de dados

num = int(input("Informe o número: "))

# Processamento dos dados

if num % 2 == 0:
    print("%d é um número par. " %num)
else:
    print("%d não é um número par. " %num)


