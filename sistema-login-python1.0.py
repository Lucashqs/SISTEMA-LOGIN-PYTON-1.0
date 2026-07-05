usuarios = []
senhas = []

while True:
    print("\n--- SISTEMA ---")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        senha = input("Digite a senha: ")

        usuarios.append(nome)
        senhas.append(senha)

        print("Usuário cadastrado!")

    elif opcao == "2":
        nome = input("Usuário: ")
        senha = input("Senha: ")

        if nome in usuarios:
            index = usuarios.index(nome)

            if senhas[index] == senha:
                print("Login realizado com sucesso!")
            else:
                print("Senha incorreta!")
        else:
            print("Usuário não encontrado!")

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")