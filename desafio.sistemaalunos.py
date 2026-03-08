#O programa deve permitir cadastrar vários alunos

N_alunos=int(input("insira o número de alunos: "))
alunos=[]
nome_unicos=set()

for an in range(N_alunos):

    nomes=input("insira o nome do aluno: ")

    if nomes in nome_unicos:
        print("nome já cadastrado")

    else:
        nome_unicos.add(nomes)
#idade
        idade=int(input("insira a idade do aluno: "))
# notas dos alunos
        notas=[]
        for i in range(3):
            nota=float(input(f"nota {i+1}: "))
            notas.append(nota)

        notas=tuple(notas)
        dados=(nomes, idade, notas)
        alunos.append(dados)

print(alunos)