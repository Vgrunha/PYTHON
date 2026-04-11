#Gestão de compras/vendes livros

from colorama import init, Fore
init(autoreset=True)

informacao_clientes = {
    'nome': [],
    'idade': [],
    'morada': [],
    'línguagem do livro': [],
    'forma de pagamento': [],
    'quantidade': []
}


def menu():
    print(" BEM-VINDO AO MENU \nInformação importante: (C = Cliente, V = Vendedor)")
    opção = input("Selecione entre 'C' ou 'V': ").upper()

    if opção == 'C':
        print(Fore.LIGHTYELLOW_EX+"<= ABA CLIENTE =>")
        compra = int(input("quantidades de livros que gostaria de comprar: "))

        while compra < 1 or compra > 30:
            print(Fore.RED + "QUANTIDADE NÃO PERMITIDA")
            compra = int(input("Introduza a quantidade permitida: "))

        print(Fore.GREEN + "QUANTIDADE ACEITA")

        nomes = input("NOME: ")
        idades = int(input("IDADE: "))
        moradia = input("MORADA: ")
        idioma = input("Selecione idioma: ")
        formaPagar = input("Selecione a forma de pagamento: ")

        informacao_clientes["nome"].append(nomes)
        informacao_clientes["idade"].append(idades)
        informacao_clientes["morada"].append(moradia)
        informacao_clientes["línguagem do livro"].append(idioma)
        informacao_clientes["forma de pagamento"].append(formaPagar)

        print("\n Verifique a informação guardada:")
        for chave, valor in informacao_clientes.items():
            print(f"{chave}: {valor}")

        finalizar = input("Selecione 'F' para finalizar a compra ou 'S' para sair: ").upper()

        if finalizar == 'F':
            print(Fore.CYAN + "Compra finalizada! Obrigado pela sua compra ")
        elif finalizar == 'S':
            print(Fore.CYAN + " A voltar ao menu...")
        
    elif opção == 'V':
        voltar_menu = False # iniciar o loop 

        while voltar_menu == False:
            print("<= ABA VENDEDOR =>")
            print("1 - Ver clientes")
            print("2 - Procurar cliente")
            print("3 - informação de venda")
            print("4 - Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                print("\n LISTA DE CLIENTES:")
                if len(informacao_clientes["nome"]) == 0:
                    print(Fore.RED + "Nenhum cliente registado")
                else:
                    for i in range(len(informacao_clientes["nome"])):
                        print(Fore.LIGHTMAGENTA_EX+f"\nCliente {i+1}:")
                        print(f"Nome: {informacao_clientes['nome'][i]}")
                        print(f"Idade: {informacao_clientes['idade'][i]}")
                        print(f"Morada: {informacao_clientes['morada'][i]}")
                        print(f"Idioma: {informacao_clientes['línguagem do livro'][i]}")
                        print(f"Pagamento: {informacao_clientes['forma de pagamento'][i]}")

            elif opcao == '2':
                nome_procura = input("Digite o nome do cliente: ")
                if nome_procura in informacao_clientes["nome"]:
                    i = informacao_clientes["nome"].index(nome_procura)
                    print("\n Cliente encontrado:")
                    print(f"Nome: {informacao_clientes['nome'][i]}")
                    print(f"Idade: {informacao_clientes['idade'][i]}")
                    print(f"Morada: {informacao_clientes['morada'][i]}")
                    print(f"Idioma: {informacao_clientes['línguagem do livro'][i]}")
                    print(f"Pagamento: {informacao_clientes['forma de pagamento'][i]}")
                else:
                    print(Fore.RED + "Cliente não encontrado")

        
            elif opcao == '3':
                print("1 - Média de vendas")
                print("2 - Média da idade dos clientes")
                print("3 - Média de quantidade de livros vendidos")
                
                opcao2=input("Escolha uma opção: ")
                if opcao2 == "1":
                    # Média de vendas 
                    if len(informacao_clientes["quantidade"]) == 0:
                        print(Fore.RED + "Sem vendas ainda")
                    else:
                        total = sum(informacao_clientes["quantidade"])
                        print(Fore.GREEN + f"Total de livros vendidos: {total}")
                elif opcao2 == "2":
                    # Média de idade
                    if len(informacao_clientes["idade"]) == 0:
                        print(Fore.RED + "Sem clientes registados")
                    else:
                        media = sum(informacao_clientes["idade"]) / len(informacao_clientes["idade"])
                        print(Fore.GREEN + f"Média de idades: {media:.2f}")
                elif opcao2 == "3":
                    # Média de livros por cliente
                    if len(informacao_clientes["quantidade"]) == 0:
                        print(Fore.RED + "Sem dados de vendas")
                    else:
                        media = sum(informacao_clientes["quantidade"]) / len(informacao_clientes["quantidade"])
                        print(Fore.GREEN + f"Média de livros por cliente: {media:.2f}")

                else:
                    print(Fore.RED + "Opção inválida")

            elif opcao == '4':
                print("Voltando ao menu principal...")
                voltar_menu = True   # sai do loop

            else:
                print(Fore.RED +"Opção inválida")


# LOOP PRINCIPAL
while True:
    menu()
        

