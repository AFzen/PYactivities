# Programa para verificar classe eleitoral

print ("## PROGRAMA PARA VERIFICAÇÃO DE CLASSE ELEITORAL #")

print () #Blank Line

# Entrada de dados

nome = str(input("Informe o seu nome. "))
idade = int(input("Informe a sua idade. "))

# Processamento dos dados

if idade >= 16:
    if idade in range(18, 65, 1):
        print("%s você é eleitor obrigatório. " %nome)
    if idade in range(16, 17, 1) or idade > 65:
        print("%s você é eleitor facultativo. " %nome)
else:
    print("%s você não é eleitor. " %nome)


