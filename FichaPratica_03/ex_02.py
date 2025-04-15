menu = 0
for _ in range(100):

    menu =int(input("Insira o numero correspondente á opção desejada"))

    if menu == 1:
        print("Criar")
    elif menu == 2:
        print("Atualizar")
    elif menu == 3:
        print("Eliminar")
    elif menu == 4:
        print("Sair")
    elif menu < 1 or menu > 4:
        print("Opçao invalida digite entre 1 e 4")
