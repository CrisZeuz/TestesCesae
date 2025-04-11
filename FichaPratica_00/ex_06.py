Valor1=int(input("insira o valor1"))
Valor2=int(input("insira o valor2"))

TemporariaV= Valor1
Valor1=Valor2
valor2=TemporariaV

Valor1, Valor2 = Valor2, Valor1

print("valor1=", Valor1)
print("valor1=", Valor2)
