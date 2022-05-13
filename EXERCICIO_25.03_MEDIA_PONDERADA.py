#Programa que calcula a média ponderada entre 3 notas

print ("## CALCULADORA DE MÉDIA PONDERADA ##")
print () # Blank Line 

#Entrada de dados

aluno = str(input("Qual é o nome do aluno? "))
p1 = int(input("Qual é o peso da nota 1? "))
p2 = int(input("Qual é o peso da nota 2? "))
p3 = int(input("Qual é o peso da note 3? "))

n1 = float(input("Qual é a nota 1? "))
n2 = float(input("Qual é a nota 2? "))
n3 = float(input("Qual é a nota 3? "))

#Processamento dos dados

mp = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3)

#Saida de dados

print ("A média do aluno {} é: " .format(aluno), "%.2f" %mp)







