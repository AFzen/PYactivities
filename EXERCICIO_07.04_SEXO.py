#Programa para ler sexo da pessoa e exibir se é homem ou mulher

nome = str(input("Qual o seu nome? "))

sexo = str(input("Qual o seu sexo? (M/F) "))

sexo = sexo.upper()

if sexo == "M":
    print(nome, "você é homem. ")
if sexo == "F":
    print(nome, "você é mulher. ")



