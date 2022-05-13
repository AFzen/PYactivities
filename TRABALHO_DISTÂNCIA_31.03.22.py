# Programa para calcular o tempo de viagem

print ("## PROGRAMA PARA CALCULAR TEMPO DE VIAGEM ##")

print () #Blank Line

# Entrada de dados

dist = float(input("Qual é a distância que você quer percorrer na viagem? (Km) "))

print () #Blank Line

vmedia = int(input("Qual é a velocidade média do veículo? (Km/h) "))

print () #Blank Line

# Processamento dos dados

tempo = (dist / vmedia)

# Saída de dados

print ("O tempo de viagem estimado é de %.4f horas. " % tempo)

