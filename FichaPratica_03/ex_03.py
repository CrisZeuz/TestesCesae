jogador1=int(input("Jogador 1 Insira um valor entre 0 e 100: "))
jogador2=int(input("Adivinhe o valor que o Jogador 1 colocou: "))
contador = 1

while jogador2 != jogador1:
    if jogador2 > jogador1:
            print("O seu palpite está acima do Valor oculto")
    elif jogador2 < jogador1:
            print("O seu plapite está abaixo do Valor Oculto")
            
    jogador2=int(input("Tente de novo: "))
    contador += 1
print(f"Boa! adivinhou o Valor Oculto, utilizando:",{contador} ,"tentativa(s).")