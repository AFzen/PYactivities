# Programa para calcular se uma pessoa é adulta

# Condições para ser adulto:
# Homem >= 18 anos
# Mulher >= 21 anos

print ("## PROGRAMA PARA SABER SE UMA PESSOA É ADULTA #")
print () #Blank Line

# Entrada de dados

nome = str(input("Qual é o seu nome? "))
print()
sexo = str(input("Qual é o seu sexo? (M/F) "))
print()
idade = int(input("Qual é a sua idade? "))
print()

# Processamento dos dados

sexo = sexo.upper()

if sexo == "M":
    if idade >=  18:
        print("%s você é adulto. " %nome)
    else:
        print("%s você não é adulto. " %nome)
else:
    if  idade >= 21:
        print("%s você é adulto. " %nome)
    else:
        print("%s você não é adulto. " %nome)
