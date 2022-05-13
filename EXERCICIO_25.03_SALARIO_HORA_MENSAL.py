#Programa para calcular salário no mês

print ("## CALCULADORA DE SALÁRIO ##")
print () # Blank Line

#Entrada de dados

nome = str(input("Qual é o seu nome? "))
porhora = float(input("Qual é o valor ganho por hora? "))
horas = float(input("Quantas são as horas trabalhadas no mês?  "))

p1 = str(input("O valor de horas é inteiro? YES/NO "))

if p1 == 'NO':
    min = float(input("Quantos minutos? "))
    horas = (min/60) + horas
else:
    print () # Blank Line

salario = (porhora * horas)

#Saida de dados

print ("O total que", nome, "deve receber no mês é de R$%.2f" %salario)
