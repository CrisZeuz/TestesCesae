num=int(input("insira um numero:"))

max = num +5
min = num -5

while min <= max:
    if min != num:
        print(min)
    min +=1