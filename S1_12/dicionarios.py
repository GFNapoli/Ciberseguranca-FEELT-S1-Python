def exercicio1():
    ativo = {'nome':'Servidor', 'ip':'128.0.0.1/22', 'os':'debian', 'criticidade':'alta', 'batata':''}
    print(ativo)
    print(ativo.get('criticidade'))
    print(ativo.keys())
    print(ativo.items())
    print(ativo.get('ip', 'não existe'))
    ativo.popitem()
    print(ativo)
    ativo['batata'] = 'frita'
    ativo['manga']='one piece'
    print(ativo)
    ativo.pop('batata')
    print(ativo)

exercicio1()

def exercicio2():
    ativo = {}

    print('Cadastrando novo ativo:')
    nome = input('Insira o nome do ativo\n>> ')
    ip = input('Insira o IP\n>> ')
    os = input('Insira o sitema operacional\n>> ')
    criticidade = input('Insira a criticidade do ativo\n>> ')

    ativo['nome'] = nome
    ativo['ip'] = ip
    ativo['os'] = os
    ativo['criticidade'] = criticidade

    print(ativo)

    print('\nAtualize a criticidade')
    criti = input('Digite a nova criticidade\n>> ')
    ativo['criticidade'] = criti

    print(ativo)

exercicio2()

def exercicio3():
    ativo = {'nome': 'Servidor', 'ip': '128.0.0.1/22', 'os': 'debian', 'criticidade': 'alta'}
    chaves = list(ativo.keys())
    valores = list(ativo.values())
    print(chaves)
    print(valores)

    print('{} é {}\n{} é {}\n{} é {}\n{} é {}'.format(chaves[0], valores[0], chaves[1], valores[1], chaves[2], valores[2], chaves[3], valores[3]))
exercicio3()