while True:

    for i in range(1, 11):
        print(i)

    try:
        sair = int(input("O que deseja fazer agora?\n1 - Sair\n2 - Continuar\n3 - Outro\n>> "))
    except ValueError:
        print('Valor invalido digitado, repetindo')
        continue

    if sair==1 :
        break
    elif sair==2 :
        continue
    elif sair==3 :
        print('Brincadeira não existe outra opção então vamos recomeçar XD')
    else:
        print('Digitou errado voltando ao começo!!!')