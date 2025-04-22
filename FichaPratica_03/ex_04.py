
num = int(input("Insira um Numero: "))



if num <= 1:
    print("Não é primo")
else:
    contador = 0

    for i in range(1, num +1):
        if num % i == 0:
            contador +=1
    if contador == 2:
        print("É Primo")
    else:
        print("não é primo")
