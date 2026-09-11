while True:
    continuar = input('Deseja informar alguma vulnerabilidade? (s/n) ')
    if continuar == 's' or continuar == 'S':
        while True:
            vulnerabilidade = input('Digite a severidade de sua vulnerabilidade: ')
            if vulnerabilidade == 'baixa':
                print('Vulnerabilidade baixa fique tranquilo, resolva quando puder')
                break
            elif vulnerabilidade == 'média':
                print('Vulnerabilidade média fique de olho, resolva assim que puder')
                break
            elif vulnerabilidade == 'alta':
                print('Vulnerabilidade alta, resolva o mais rapido possivel')
                break
            elif vulnerabilidade == 'crítica':
                print('Vulnerabilidade crítica perigo, Resolva imediatamente')
                break
            else:
                print('Digite um valor valido entre baixa, média, alta ou crítica')

    elif continuar == 'n' or continuar == 'N':
        print('Obrigado por usar o sistema! Ate logo!')
        break
    else:
        print('Digite um valor valido entre S, N!!')