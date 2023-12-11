

LIMITE_SAQUE = 500
extrato = []
numero_saques = 3
saldo = 1500

while True:

    print(f"""
    [1] - Sacar
    [2] - Depositar
    [3] - Extrato
    [4] - Sair

    Selecione a opcao desejada
    """)

    opcao = input() 

    if opcao == '1':
        print("\n")

        if numero_saques > 0:
            print('Informe o valor a ser sacado: ')
            valor_sacado = float(input())
            print("\n")
            
            if valor_sacado <= saldo and valor_sacado <= LIMITE_SAQUE and valor_sacado > 0:
                print(f'Saque de {valor_sacado} realizado', end="\n")

                extrato.append(f'-R$ {valor_sacado:.2f}')
                saldo -= valor_sacado
                numero_saques -= 1
            
            elif valor_sacado > LIMITE_SAQUE:
                print('Valor a ser sacado acima do limite diario', end="\n")

            elif valor_sacado > saldo:
                print('Saldo insuficiente', end="\n")

        else:
            print('Limite de saques diarios atingido', end="\n")

    elif opcao == '2':
        print("\n")
        print('Informe o valor a ser depositado: ')
        valor_depositado = float(input())
        print("\n")

        if valor_depositado > 0:
            saldo += valor_depositado
            extrato.append(f'+R$ {valor_depositado:.2f}')
            print(f'Depositado o valor de R${valor_depositado:.2f}', end="\n")

        else:
            print('Valor nao pode ser negativo', end="\n")

    elif opcao == '3':
        print("\n")
        print("================ Extrato ================")

        for i in range(0,len(extrato)):
            print(f'Movimentacao {i+1}: {extrato[i]}', end="\n")

        print("\n")
        print(f'Saldo atual em conta R$ {saldo}')

        print("=========================================")

    elif opcao == '4':
        print("\n")
        break

    else:
        print("\n")
        print('Selecione uma opcao valida', end="\n")
        

