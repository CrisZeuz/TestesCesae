#0-25
contador1 = 0
#26-50
contador2 = 0 
#51-75
contador3 = 0
#76-100
contador4 = 0

intervalo = int(input("insira um numero positivo"))


while True:
    intervalo = int(input("insira um numero positivo"))
    if intervalo < 0:
        break
    if 0 <= intervalo <=25:
        contador1 += 1
    elif 26 >= intervalo <= 50:
        contador2 += 1
    elif 51 <= intervalo <= 75:
        contador3 +=1
    elif 76 <= intervalo <= 100:
        contador4 +=1



print("[0-25]",contador1)
print("[26-50]",contador2)
print("[51-75]",contador3)
print("[76-100]",contador4)