from enum import Enum

class severidade(Enum):
    baixa = 1
    media = 2
    alta = 3
    critica = 4

    def get_by_number(numero):
        if numero == severidade.baixa.value:
            return severidade.baixa
        if numero == severidade.media.value:
            return severidade.media
        if numero == severidade.alta.value:
            return severidade.alta
        if numero == severidade.critica.value:
            return severidade.critica

class status(Enum):
    ativo = 1
    inativo = 2
    em_manutencao = 3

    def get_by_number(numero):
        if numero == status.ativo.value:
            return status.ativo
        if numero == status.inativo.value:
            return status.inativo
        if numero == status.em_manutencao.value:
            return status.em_manutencao


def adicionar():
    base_ativo = {}
    nome = input('Adicione um item\n>> ')
    sta = int(input('Qual o status? 1 - ativo, 2 - inativo , 3 - em_manutencao\n>>'))
    sev = int(input('Qaul a severidade? 1 - baixa, 2 - media, 3 - alta, 4 - critica\n>>'))

    base_ativo['nome'] = nome
    base_ativo['status'] = status.get_by_number(sta)
    base_ativo['severidade'] = severidade.get_by_number(sev)
    return base_ativo

def alterar_severidade():
    sev = int(input('Qaul a severidade? 1 - baixa, 2 - media, 3 - alta, 4 - critica\n>>'))
    return sev

def alterar_status():
    sta = int(input('Qual o status? 1 - ativo, 2 - inativo , 3 - em_manutencao\n>>'))
    return sta

def listar(lista_ativos):
    print('----------------|----------------')
    for i in range(len(lista_ativos)):
        print(i, '{} - status:{} | severidade:{}'.format(lista_ativos[i]['nome'], lista_ativos[i]['status'].name, lista_ativos[i]['severidade'].name))
    print('----------------|----------------')

def buscar_by_name(lista_ativos, nome):
    for i in range(len(lista_ativos)):
        if lista_ativos[i]['nome'] == nome:
            return i

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
    ativo1 = {'nome': 'servidor', 'status': status.ativo, 'severidade': severidade.alta}
    ativo2 = {'nome': 'notebook', 'status': status.em_manutencao, 'severidade': severidade.baixa}

    lista_ativo = [ativo1, ativo2]
    print('Bem vindo ao listas 1.0')
    mensagem_despedida = 'Obrigado por usar nossos serviços, ate a proxima!!'
    while True:
        try:
            opcao = int(input('O que deseja fazer?\nEscolha a função que melhor lhe ajudar\n'
                              '1 - Exibir lista de Ativos\n'
                              '2 - Adicionar ativo\n'
                              '3 - Alterar status ativo\n'
                              '4 - Alterar severidade ativo\n'
                              '5 - Sair\n>> '))

            if opcao == 1:
                listar(lista_ativo)
            elif opcao == 2:
                aux = adicionar()
                lista_ativo.append(aux)
                print(lista_ativo)
            elif opcao == 3:
                nome = input('Qual nome do ativo que vc deseja mudar o status?\n>> ')
                lista_ativo[buscar_by_name(lista_ativo, nome)]['status'] = status.get_by_number(alterar_status())
            elif opcao == 4:
                nome = input('Qual nome do ativo que vc deseja mudar a severidade?\n>> ')
                lista_ativo[buscar_by_name(lista_ativo, nome)]['severidade'] = severidade.get_by_number(alterar_severidade())
            elif opcao == 5:
                print(mensagem_despedida)
                break
            else:
                print('Opção invalida tente novamente')

        except ValueError:
            print('Por valor digite um valor entre 1, 2 ou 3')

main()