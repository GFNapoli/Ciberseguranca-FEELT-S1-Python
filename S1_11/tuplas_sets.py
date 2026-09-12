def tuplas():
    tupla = ('Servidor', 'notebook', 'gabinete', 'Firewall')
    print(tupla[2])
    (servidor, transporte, mesa, protecao) = tupla
    print(mesa, transporte)

#tuplas()

def continuar(texto):
    while True:
        opcao = input('{}\n>> '.format(texto))
        opcao = opcao.lower()
        if opcao == 's':
            return True
        elif opcao == 'n':
            return False
        else:
            print('Opção ivalida!! Tente novamente!')

def funcao_sets():
    vulnerabilidades = set()
    while True:
        vulnerabilidade = input('\nDigite uma vulnerabilidade\n>> ')
        vulnerabilidades.add(vulnerabilidade)
        if not continuar('Deseja adicionar mais??(s/n)'):
            break

    print('Resultado')
    print(vulnerabilidades)

#funcao_sets()

def compara_sets():
    conjunto1 = {'Baixa', 'Media'}
    conjunto2 = {'Media', 'Alta', 'Critica'}

    #união dos sets
    print(conjunto1 | conjunto2)

    #interseção
    print(conjunto1 & conjunto2)

    #diferença
    print(conjunto2 - conjunto1)

compara_sets()