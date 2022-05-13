#Acumulador

n = int(input("Quantos números? "))
print ()
cont = 1
soma = 0

while cont <= n:

    num = int(input("Informe o %d número: " %cont))
    soma = soma + num
    print ()

    cont = cont + 1

print ("A soma é {} " .format(soma))
print ()
print ("FIM")
print ()







