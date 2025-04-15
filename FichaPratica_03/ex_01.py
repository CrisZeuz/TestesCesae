#valores para operação mais caracter

pergunta = "y"


while pergunta == "y":
    num1 = float(input("insira um numero"))
    num2 = float(input("insira um numero"))
    operação = input("insira o simbolo da operação +,-,/,*")
    if operação == "+":
        print(num1+num2)
    elif operação == "-":
        print(num1-num2)
    elif operação == "/":
        print(num1/num2)
    elif operação == "*":
        print(num1*num2)

    pergunta = input("quer continuar as operações? /y/n/")

