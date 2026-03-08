#gerador de apostas
    #1 leitor de aposta ate 5 apostas
    #1 aposta tem 5 nº e 2 estrelas
#quantas apostas quer jogar?
    #aposta -- tupla
    #nº,estrela -- set
    #boletim -- lista

import random

ap=int(input("Quantas apostas quer jogar?: "))
boletim=[]

if ap<1 or ap>5:
    print(" -= NÚMERO DE APOSTA INDISPONIVEL =- ")
else:
    for n in range(ap):
        numeros=set()       #set vazio; não pode ser numeros={} porque interpreta como sendo um dicionário
        estrelas=set()      #set vazio; não pode ser estrela={} porque interpreta como sendo um dicionário
        while len(numeros)<5:
            numeros.add(random.randint(1,50))
        while len(estrelas)<2:
            estrelas.add(random.randint(1,12))
        aposta=(numeros,estrelas)
        boletim.append(aposta)

    for i in range(ap): # percorre cada aposta
        '''aposta=boletim[i] # tupla
        numeros=aposta[0]
        estrelas=aposta[1]'''
        numeros,estrelas=boletim[i] # tupla 
        
        print(f'aposta {i+1}: ',end="")
        lista=list(numeros)
        lista.sort() #sort não devolve 
       
        for n in lista:
            print(f"{n:02d} ",end="")
        print("+ ",end="")
        lista=list(estrelas)
        lista.sort()
        for n in lista:
            print(f"{n:02d} ",end="")
        print()
