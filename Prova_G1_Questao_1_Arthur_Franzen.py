#Arthur Fattori Franzen

cp = int(input("Informe o código do produto: "))
quant = int(input("Informe a quantidade de produtos: "))

if cp == 24:
    pfinal = (12.9 * quant)
else: 
    if cp == 32:
        pfinal = (3.5 * quant)
    else:
        pfinal = (22 * quant)

print ("O valor total dos produtos é de R$%.2f " %pfinal)

