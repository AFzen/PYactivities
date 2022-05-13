# ARTHUR FATTORI FRANZEN

nome = str(input("Qual é o seu nome? "))
sexo = str(input("Qual é o seu sexo? (M/F) "))
idade = int(input("Qual é a sua idade? "))
altura = float(input("Qual é a sua altura? (em metros) "))
peso = float(input("Qual é o seu peso? (em kg) "))

sexo = sexo.upper()

if sexo == "M":
    peso_i = ((72.7 * altura) - 58)
    diferenca_peso = peso - peso_i
    margem = peso_i * 0.05
    if idade > 65 and diferenca_peso > peso_i * 0.2:
        percentual = ((peso/(peso_i/100))-100)
        print("Cuidado! Voocê deve procurar um médico, pois está %.2f %% acima do peso. " %percentual)
    else:
        if (peso + margem) > peso_i:
            print(nome, "você deve emagrecer %.2f kg. " %diferenca_peso)
        elif (peso - margem) < peso_i:
            diferenca_peso * -1
            print(nome, "você pode engordar %.2f kg. " %diferenca_peso)
        else:
            print(nome, "você está no seu peso ideal. ")
if sexo == "F":
    peso_i = ((62.1 * altura) - 44.7)
    diferenca_peso = peso - peso_i
    margem = peso_i * 0.05
    if idade > 60 and diferenca_peso > peso_i * 0.2:
        percentual = ((peso/(peso_i/100))-100)
        print("Cuidado! Voocê deve procurar um médico, pois está %.2f%% acima do peso. " %percentual)
    else:
        if (peso + margem) > peso_i:
            print(nome, "você deve emagrecer %.2f kg. " %diferenca_peso)
        elif (peso - margem) < peso_i:
            diferenca_peso * -1
            print(nome, "você pode engordar %.2f kg. " %diferenca_peso)
        else:
            print(nome, "você está no seu peso ideal. ")


 
        
    
        

