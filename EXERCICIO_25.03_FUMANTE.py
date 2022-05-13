#Programa para calcular o total de dias de vida perdido por um fumante

cig = int(input("Quantos cigarros você fuma por dia? "))

print () # Blank Line

anos = int(input("Quantos anos fazem que você fuma? "))

print () # Blank Line

tfum = (anos * 365)
quant = (cig * tfum)

tempvida = ((quant / 60) / 24)

print ("Você perdeu %.2f dias de vida por fumar. " %tempvida)

