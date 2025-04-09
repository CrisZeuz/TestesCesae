numero1=int(input("insira o peso 1"))
numero2=int(input("insira o peso 2"))
numero3=int(input("insira o valor 3"))



mediaSimples = (numero1 + numero2 + numero3) / 3
mediaPonderada = ((numero1*20) + (numero2*30) + (numero3*50)) / (20+30+50)

print("a média dos valores é =", mediaSimples)
print("o valor ponderado é =", mediaPonderada)

