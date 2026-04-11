from colorama import init, Fore
init(autoreset=True)

#Login do vendedor
VENDEDOR_USER="admin"
VENDEDOR_PASS="1234"

def login_vendedor():
    acesso=False #fecha o acesso ao utilizador 
    tentativas=0
    
    while not acesso and tentativas<3:
        user=input("Username: ")
        password=input("Password: ")
        
        if user==VENDEDOR_USER and password==VENDEDOR_PASS:
            print(Fore.GREEN+"Login bem-sucedido!")
            acesso=True #abre o acesso ao utilizador
        else:
            print(Fore.RED+"Credenciais inválidas")
            tentativas+=1 
    
    if not acesso:
        print(Fore.RED+"Acesso bloqueado")
    
    return acesso

#Dicionario de clientes
informacao_clientes={
    'nome':[],
    'idade':[],
    'morada':[],
    'linguagem':[],
    'forma de pagamento':[],
    'quantidade':[]
}

def menu():
    print("\n BEM-VINDO AO MENU ")
    print("Informação importante: (C = Cliente, V = Vendedor)")

    opcao=input("Selecione entre 'C' ou 'V' (ou 'S' para sair): ").upper()

    if opcao=='C':
        print(Fore.LIGHTYELLOW_EX+"\n<= ABA CLIENTE =>")

        valido=False
        while not valido:
            compra=input("Quantidades de livros (1-30): ")
            
            so_numeros=True
            i=0
            
            while i<len(compra):
                if compra[i]<'0' or compra[i]>'9':
                    so_numeros=False
                i+=1
            
            if so_numeros and compra!="":
                compra=int(compra)
                if 1<=compra<=30:
                    valido=True
                else:
                    print(Fore.RED+"QUANTIDADE NÃO PERMITIDA")
            else:
                print(Fore.RED+"Digite um número válido")

        print(Fore.GREEN+"QUANTIDADE ACEITA")

        nomes=input("NOME: ")

        valido=False
        while not valido:
            idades=input("IDADE: ")
            so_numeros=True
            i=0
            
            while i<len(idades):
                c=idades[i]
                if c<'0' or c>'9':
                    so_numeros=False
                i+=1
            
            if so_numeros and idades!="":
                idades=int(idades)
                if idades>0:
                    valido=True
                else:
                    print(Fore.RED+"Idade inválida")
            else:
                print(Fore.RED+"Digite um número válido")

        moradia=input("MORADA: ")
        idioma=input("Selecione idioma: ")
        formaPagar=input("Selecione a forma de pagamento: ")

        informacao_clientes["nome"].append(nomes)
        informacao_clientes["idade"].append(idades)
        informacao_clientes["morada"].append(moradia)
        informacao_clientes["linguagem"].append(idioma)
        informacao_clientes["forma de pagamento"].append(formaPagar)
        informacao_clientes["quantidade"].append(compra)

        print("\nVerifique a informação guardada:")
        for chave, valor in informacao_clientes.items():
            print(f"{chave}: {valor}")

    elif opcao=='V':
        if login_vendedor():
            voltar_menu=False

            while voltar_menu==False:
                print("\n<= ABA VENDEDOR =>")
                print("1 - Ver clientes")
                print("2 - Procurar cliente")
                print("3 - Atualizar cliente")
                print("4 - Eliminar cliente")
                print("5 - Informação de vendas")
                print("6 - Voltar ao menu principal")

                opcao=input("Escolha uma opção: ")

                if opcao=='1':
                    if len(informacao_clientes["nome"])==0:
                        print(Fore.RED+"Nenhum cliente registado")
                    else:
                        for i in range(len(informacao_clientes["nome"])):
                            print(Fore.LIGHTMAGENTA_EX+f"\nCliente {i+1}:")
                            print(f"Nome: {informacao_clientes['nome'][i]}")
                            print(f"Idade: {informacao_clientes['idade'][i]}")
                            print(f"Morada: {informacao_clientes['morada'][i]}")
                            print(f"Idioma: {informacao_clientes['linguagem'][i]}")
                            print(f"Pagamento: {informacao_clientes['forma de pagamento'][i]}")
                            print(f"Quantidade: {informacao_clientes['quantidade'][i]}")

                elif opcao=='2':
                    nome_procura=input("Digite o nome do cliente: ")
                    if nome_procura in informacao_clientes["nome"]:
                        i=informacao_clientes["nome"].index(nome_procura)
                        print("\nCliente encontrado:")
                        print(f"Nome: {informacao_clientes['nome'][i]}")
                        print(f"Idade: {informacao_clientes['idade'][i]}")
                        print(f"Morada: {informacao_clientes['morada'][i]}")
                        print(f"Idioma: {informacao_clientes['linguagem'][i]}")
                        print(f"Pagamento: {informacao_clientes['forma de pagamento'][i]}")
                    else:
                        print(Fore.RED+"Cliente não encontrado")

                elif opcao=='3':
                    nome=input("Nome do cliente a atualizar: ")
                    if nome in informacao_clientes["nome"]:
                        i=informacao_clientes["nome"].index(nome)
                        novo_nome=input("Novo nome: ")
                        if novo_nome:
                            informacao_clientes["nome"][i]=novo_nome
                        print(Fore.GREEN+"Cliente atualizado!")
                    else:
                        print(Fore.RED+"Cliente não encontrado")

                elif opcao=='4':
                    nome=input("Nome do cliente a eliminar: ")
                    if nome in informacao_clientes["nome"]:
                        i=informacao_clientes["nome"].index(nome)
                        for chave in informacao_clientes:
                            del informacao_clientes[chave][i]
                        print(Fore.GREEN+"Cliente eliminado!")
                    else:
                        print(Fore.RED+"Cliente não encontrado")

                elif opcao=='5':
                    if len(informacao_clientes["quantidade"])==0:
                        print(Fore.RED+"Sem vendas ainda")
                    else:
                        total=sum(informacao_clientes["quantidade"])
                        media=total/len(informacao_clientes["quantidade"])
                        print(Fore.GREEN+f"Total vendidos: {total}")
                        print(Fore.GREEN+f"Média por cliente: {media:.2f}")

                elif opcao=='6':
                    voltar_menu=True
                else:
                    print(Fore.RED+"Opção inválida")

    elif opcao=='S':
        print("Programa terminado")
        exit()
    else:
        print(Fore.RED+"Opção inválida")

while True:
    menu()