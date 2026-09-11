lista_ativos = ['notebook', 'monitor', 'mouse']

def listar():
    print('----------------|----------------')
    for i in range(len(lista_ativos)):
        print(i, lista_ativos[i])
    print('----------------|----------------')

def remover():
    while True:
        removido = input('Qual elemento deseja remover??\n>> ')
        if lista_ativos.__contains__(removido):
            lista_ativos.remove(removido)
            print('Item removido com sucesso!')
        else:
            print('O item não existe na lista!')
        if not continuar('Deseja remover mais algum item?(s/n)'):
            break


def adicionar():
    while True:
        novo = input('Adicione um item\n>> ')
        if not lista_ativos.__contains__(novo):
            lista_ativos.append(novo)
        else:
            print('Item já cadastrado!!')
        if not continuar('Deseja adicionar mais algum item?(s/n)'):
            break

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

def main():
    print('Bem vindo ao listas 1.0')
    mensagem_continuar = 'Deseja continuar usando a aplicação?(s/n)'
    mensagem_despedida = 'Obrigado por usar nossos serviços, ate a proxima!!'
    while True:
        try:
            opcao = int(input('O que deseja fazer?\nEscolha a função que melhor lhe ajudar\n'
                              '1 - Exibir lista de Ativos\n'
                              '2 - Adicionar ativo\n'
                              '3 - Remover ativo\n'
                              '4 - Sair\n>> '))

            if opcao == 1:
                listar()
            elif opcao == 2:
                adicionar()
            elif opcao == 3:
                remover()
            elif opcao == 4:
                print(mensagem_despedida)
                break
            else:
                print('Opção invalida tente novamente')

        except ValueError:
            print('Por valor digite um valor entre 1, 2 ou 3')

main()