def ativo():
    id_ativo = int(input('Digite o id do ativo: '))
    nome_ativo = input('Digite qual o nome do ativo: ')
    responsavel = input('Digite o nome do responsavel por esse ativo: ')
    localizacao = input('Digite seu endereço: ')

    print('\n-----------------|-----------------')
    print('O ID do ativo é: {}\nCujo ativo é: {}\nO responsavel é: {}\nLocalizado em: {}'
          .format(id_ativo, nome_ativo, responsavel, localizacao))
    print('-----------------|-----------------\n')

def severidade(vulnerabilidade):
    if vulnerabilidade == 'baixa':
        print('Vulnerabilidade baixa fique tranquilo, resolva quando puder')
    elif vulnerabilidade == 'média':
        print('Vulnerabilidade média fique de olho, resolva assim que puder')
    elif vulnerabilidade == 'alta':
        print('Vulnerabilidade alta, resolva o mais rapido possivel')
    elif vulnerabilidade == 'crítica':
        print('Vulnerabilidade crítica perigo, Resolva imediatamente')

def recebe_vulnerabilidade():
    listpossiveis = ['baixa', 'média', 'alta', 'crítica']
    while True:
        try:
            nivel = input('Por favor digite qual a vulnerabilidade: ')
            nivel = nivel.lower()
            if listpossiveis.__contains__(nivel):
                severidade(nivel)
                break
            else:
                print('Digite um valor valido entre baixa, média, alta ou crítica')
        except ValueError:
            print('Digite um valor valido entre baixa, média, alta ou crítica')

def continuar():
    while True:
        opcao = input('Deseja ir para outra opção?(s/n)\n>> ')
        opcao = opcao.lower()
        if opcao == 's':
            return True
        elif opcao == 'n':
            return False
        else:
            print('Opção ivalida!! Tente novamente!')


def menu():
    print('Bem vindo ao funcoes 1.0')
    while True:
        try:
            opcao = int(input('O que deseja fazer?\nEscolha a função que melhor lhe ajudar\n'
                            '1 - Exibir um Ativo\n'
                            '2 - Informar o nivel de vulnerabilidade\n'
                            '3 - Sair\n>> '))

            if opcao == 1:
                ativo()
                if not continuar():
                    print('Obrigado por usar nossos serviços, ate a proxima!!')
                    break
            elif opcao == 2:
                recebe_vulnerabilidade()
                if not continuar():
                    print('Obrigado por usar nossos serviços, ate a proxima!!')
                    break
            elif opcao == 3:
                print('Obrigado por usar nossos serviços, ate a proxima!!')
                break
            else:
                print('Opção invalida tente novamente')

        except ValueError:
            print('Por valor digite um valor entre 1, 2 ou 3')


menu()