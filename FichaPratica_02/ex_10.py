

limite=int(input("insira um numero"))
salto=int(input("insira um numero"))

num = 0

if limite <0:
    print("ERRO! O valor deve ser superior a 0")
elif salto <=0:
    print("ERRO! O valor deve ser superior a 0")
else:
    while num <= limite :
        print(num)
        num += salto