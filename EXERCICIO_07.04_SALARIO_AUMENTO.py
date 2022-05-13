# Programa para calcular o aumento do salário de um funcionário de acordo com o reajuste salarial

print ("## PROGRAMA PARA CALCULAR REAJUSTE SALARIAL ##")

print () #Blank Line

# Entrada de dados

salario_atual = float(input("Digite o seu salário atual: "))

# Processamento dos dados

if salario_atual <= 1212.00:
    reajuste = 1.15
else:
    reajuste = 1.1

salario_reajuste = salario_atual * reajuste

# Saída de dados

print("O salário com o reajuste é de: %.2f." %salario_reajuste)


