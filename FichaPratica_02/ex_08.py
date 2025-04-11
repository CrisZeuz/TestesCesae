soma = 0
num = 1
interacoes = 0

while num != -1:
    num=int(input("insira um numero"))
    if num != -1:
        soma += num
        interacoes +=1 
media = soma / interacoes
print("A média é:", media)