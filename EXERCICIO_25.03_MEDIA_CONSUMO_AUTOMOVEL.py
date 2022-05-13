#Programa que calcula a média de consumo de um automóvel

print ("## CALCULADORA DE MÉDIA DE CONSUMO ##")
print () # Blank Line

#Entrada de dados

dist = float(input("Qual foi a distância percorrida? (Km) "))
consumo = float(input("Quanto combustível foi gasto? (L) "))

#Processamento dos dados

media = (dist / consumo)

#Saida de dados

print ("O consumo médio foi de %.2fKm/L" %media)


