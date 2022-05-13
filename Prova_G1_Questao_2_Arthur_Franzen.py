#Arthur Fattori Franzen

nome = str(input("Informe seu nome: "))
p1 = float(input("Informe a nota da prova 1: "))
p2 = float(input("Informe a nota da prova 2: "))

media = ((p1 + p2)/2)

if media < 4:
    print (nome, "Sua média final é %.2f você foi reprovado por média. " %media)
else:
    if media >= 8:
        print (nome, "Sua média final é %.2f você foi aprovado por média. " %media)
    else:
        print("Você não alcançou a média, terá que fazer o exame.")
        exame = float(input("Informe a nota do seu exame: "))
        if p1 > p2:
            p2 = exame
            media = ((exame + p1)/2)
            if media >= 8:
                print(nome, "Sua média final é %.2f você foi aprovado após exame. " %media)
            else:
                print(nome, "Sua média final é %.2f você foi reprovado após exame. " %media)
        else:
            p1 = exame
            media = ((exame + p2)/2)
            if media >= 8:
                print(nome, "Sua média final é %.2f você foi aprovado após exame. " %media)
            else:
                print(nome, "Sua média final é %.2f você foi reprovado após exame. " %media)
    
