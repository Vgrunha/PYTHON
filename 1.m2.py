from colorama import init, Fore, Style
init(autoreset=True)

temp = float(input('temp: '))

if temp <= 3 or temp >= 20:
    print(Fore.RED + 'temp fora do padrão')
    print(Fore.YELLOW + 'processo de eco:')
    print(Fore.YELLOW + ' - o processo eco auto desligará o ciclo de resfriamento da geladeira')
    print(Fore.YELLOW + '   (para impedir que o processo eco seja ativado selecione a opção stop)')
    print(Fore.YELLOW + '   caso contrário o processo eco irá ser inicializado')

    ciclos = input(Fore.CYAN + 'selecione stop (se não quiser impedir selecione 0): ' + Style.RESET_ALL)

    if ciclos == '0':
        print(Fore.MAGENTA + 'processo em andamento')
    elif ciclos == 'stop':
        print(Fore.GREEN + 'processo eco impedido')
else:
    print(Fore.GREEN + 'temp estável')

#lista de comidas na geladeira
lista_comida= ['manteiga','ovo','leite','frutas']
lista_comida.append("ovo")
lista_comida.append("sopa")

print(Fore.GREEN + f'lista de comida {lista_comida}')

sem=set(lista_comida)
print(Fore.MAGENTA + f'lista de comida {lista_comida}')

