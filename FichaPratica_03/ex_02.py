
for _ in range(100):
    print("Menu de opções: \n 1 Criar \n 2 Atualizar \n 3 Eliminar \n 4 Sair")
    menu = input("Escolha a opção desejada: ")

    if menu == "1":
        print("Criar")
    elif menu == "2":
        print("Atualizar")
    elif menu == "3":
        print("Eliminar")
    elif menu == "4":
        print("Sair")
        break
    else:
        print("Opçao invalida digite entre 1 e 4")
