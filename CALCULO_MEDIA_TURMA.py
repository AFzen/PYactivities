#Média dos alunos

nro_alunos = int(input("Quantos alunos tem a turma? "))

x  = nro_alunos

cont = 1

while cont <= x :

    nome = str(input("Informe o nome: "))
    print ()
    n1 = float(input("Informe a nota 1: "))
    print ()
    n2 = float(input("Informe a nota 2: "))
    print ()
    med = (n1+n2)/2
    print ("A média de {} é %.2f " .format(nome) %med)
    print ()

    cont = cont + 1







