
#Exibe os números pares de 0 até N, sendo N um número informado pelo usuário

n = int(input("Informe o número: "))

cont = 1

while cont <= n:

    if (cont % 2) == 0:
        print (cont)
    
    cont = cont +1
