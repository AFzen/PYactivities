# Programa para calcular multa por excesso de velocidade

print ("## PROGRAMA PARA CALCULAR MULTA POR EXCESSO DE VELOCIDADE #")

print () #Blank Line

# Entrada de dados

vel = int(input("Qual é a velocidade do seu carro? (km/h) "))

# Processamento dos dados

if vel > 80:
    resto = vel -80
    multa = resto * 8
    print("Você está acima do limite de velocidade, será multado em R$%.2f " %multa)
else:
    print("Você está abaixo do limite de velocidade. ")
