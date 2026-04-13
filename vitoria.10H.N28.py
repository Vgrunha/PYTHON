#GESTÃO DE COMPRA E DADOS DO LIVRO(valentina)



from datetime import date
from colorama import init, Fore
init(autoreset=True)

VENDEDOR_USER="admin"
VENDEDOR_PASS="1234"

preco=14.99

informacao_clientes={
    "nome":[],
    "idade":[],
    "morada":[]
}

vendas={
    "linguagem":[],
    "n_contribuinte":[],
    "quantidade":[],
    "forma de pagamento":[]
}

dias_venda=[] #lista para ver o total de vendas


def login_vendedor():
    acesso=False
    tentativas=0

    while not acesso and tentativas<3:
        user=input("Username: ")
        password=input("Password: ")

        if user==VENDEDOR_USER and password==VENDEDOR_PASS:
            print(Fore.GREEN+"Login bem-sucedido!")
            acesso=True
        else:
            print(Fore.RED+"Credenciais inválidas")
            tentativas+=1

    if not acesso:
        print(Fore.RED+"Acesso bloqueado")

    return acesso


def menu():
    print("\nBEM-VINDO AO MENU")
    print("C=Cliente | V=Vendedor | S=Sair")
    opcao=input("Escolha: ").upper()

    # ================= CLIENTE =================
    if opcao=="C":
        print(Fore.LIGHTYELLOW_EX+"\n<= CLIENTE =>")
        print(f"Preço: {preco}€")

        compra_valida=False
        while not compra_valida:
            compra=input("Quantidade (1-30): ")

            if compra.isdigit():
                compra=int(compra)
                if 1<=compra<=30:
                    vendas["quantidade"].append(compra)
                    compra_valida=True
            if not compra_valida:
                print(Fore.RED+"Quantidade inválida")

        print(Fore.GREEN+"Quantidade aceite")

        nome=input("Nome: ")
        informacao_clientes["nome"].append(nome)

        idade_valida=False
        while not idade_valida:
            data=input("Nascimento (YYYY/MM/DD): ").split("/")

            if len(data)==3:
                try:
                    ano=int(data[0])
                    mes=int(data[1])
                    dia=int(data[2])

                    hoje=date.today()
                    idade=hoje.year-ano

                    if (hoje.month,hoje.day)<(mes,dia):
                        idade-=1

                    informacao_clientes["idade"].append(idade)
                    idade_valida=True
                except:
                    pass

            if not idade_valida:
                print(Fore.RED+"Data inválida")

        print("Idade:",idade)

        morada=input("Morada: ")
        informacao_clientes["morada"].append(morada)

        idioma=input("Idioma (pt/en/zh-cn/es/ko): ").lower()

        if idioma in ["pt","en","zh-cn","es","ko"]:
            vendas["linguagem"].append(idioma)
        else:
            vendas["linguagem"].append("inválido")

        nif_valido=False
        while not nif_valido:
            contribuinte=input("NIF (9 dígitos): ")

            if contribuinte.isdigit() and len(contribuinte)==9:
                numeros=[int(d) for d in contribuinte]

                soma=0
                i=0
                while i<8:
                    soma+=numeros[i]*(9-i)
                    i+=1

                resto=soma%11
                controlo=0 if resto<2 else 11-resto

                if numeros[8]==controlo:
                    vendas["n_contribuinte"].append(int(contribuinte))
                    nif_valido=True

            if not nif_valido:
                print(Fore.RED+"NIF inválido")

        pagamento=input("Pagamento (cartão/dinheiro): ").lower()

        if pagamento in ["cartão","dinheiro"]:
            vendas["forma de pagamento"].append(pagamento)
        else:
            vendas["forma de pagamento"].append("inválido")

        dias_venda.append(str(date.today()))

        finalizar=input("F para finalizar / S para sair: ").upper()

        if finalizar=="F":
            i=len(informacao_clientes["nome"])-1

            print("\nResumo:")
            print("Nome:",informacao_clientes["nome"][i])
            print("Idade:",informacao_clientes["idade"][i])
            print("Morada:",informacao_clientes["morada"][i])

            total=vendas["quantidade"][i]*preco
            print(f"Total: {total:.2f}€")

        elif finalizar=="S":
            print("Programa terminado")
            return

    # ================= VENDEDOR =================
    elif opcao=="V":
        if login_vendedor():

            sair=False
            while not sair:

                print("\n1-Ver clientes")
                print("2-Procurar NIF")
                print("3-Eliminar por NIF")
                print("4-Estatísticas")
                print("5-Sair")

                op=input("Opção: ")

                # VER CLIENTES
                if op=="1":
                    i=0
                    if len(informacao_clientes["nome"])==0:
                        print(Fore.RED+"Sem clientes")
                    else:
                        while i<len(informacao_clientes["nome"]):
                            print("\nCliente",i+1)
                            print("Nome:",informacao_clientes["nome"][i])
                            print("Idade:",informacao_clientes["idade"][i])
                            print("Morada:",informacao_clientes["morada"][i])
                            print("Quantidade:",vendas["quantidade"][i])
                            i+=1

                # PROCURAR
                elif op=="2":
                    NIF=input("NIF: ")
                    encontrado=False

                    for i in range(len(vendas["n_contribuinte"])):
                        if str(vendas["n_contribuinte"][i])==NIF:
                            print("Nome:",informacao_clientes["nome"][i])
                            print("Idade:",informacao_clientes["idade"][i])
                            print("Morada:",informacao_clientes["morada"][i])
                            print("Quantidade:",vendas["quantidade"][i])
                            encontrado=True

                    if not encontrado:
                        print(Fore.RED+"Não encontrado")

                # ELIMINAR SEM BREAK
                elif op=="3":
                    NIF=input("NIF: ")

                    novos_indices=[]
                    i=0

                    while i<len(vendas["n_contribuinte"]):
                        if str(vendas["n_contribuinte"][i])!=NIF:
                            novos_indices.append(i)
                        i+=1

                    if len(novos_indices)==len(vendas["n_contribuinte"]):
                        print(Fore.RED+"Não encontrado")
                    else:
                        for chave in informacao_clientes:
                            temp=[]
                            j=0
                            while j<len(novos_indices):
                                temp.append(informacao_clientes[chave][novos_indices[j]])
                                j+=1
                            informacao_clientes[chave]=temp

                        for chave in vendas:
                            temp=[]
                            j=0
                            while j<len(novos_indices):
                                temp.append(vendas[chave][novos_indices[j]])
                                j+=1
                            vendas[chave]=temp

                        print(Fore.GREEN+"Cliente eliminado")

                # ESTATÍSTICAS
                elif op=="4":
                    print("\n=== ESTATÍSTICAS ===")

                    total=sum(vendas["quantidade"])*preco
                    print("Total vendas:",total,"€")

                    print("\nVendas por dia:")
                    dias_unicos=[]
                    i=0

                    while i<len(dias_venda):
                        if dias_venda[i] not in dias_unicos:
                            dias_unicos.append(dias_venda[i])
                        i+=1

                    i=0
                    while i<len(dias_unicos):
                        print(dias_unicos[i])
                        i+=1

                    if len(informacao_clientes["idade"])>0:
                        media=sum(informacao_clientes["idade"])/len(informacao_clientes["idade"])
                        print("Média idades:",media)
                    else:
                        print("Sem clientes")

                elif op=="5":
                    sair=True

    elif opcao=="S":
        print("Fim")
        exit()

    else:
        print(Fore.RED+"Opção inválida")


while True:
    menu()