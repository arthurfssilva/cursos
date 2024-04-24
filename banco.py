print("    ***BEM VINDO AO BANCO RAPOSÃO***       ")

SALDO = 0
numero_saques = 0
LIMITE_SAQUES = 3
extrato = []

menu = """
    --Selecione a opção desejada-----
                1 - Saldo
                2 - Saque
                3 - Depósito
                4 - Extrato 
                5 - Sair
    ----------------------------------

                """

while True:
    opcao = input(menu)

    #SALDO
    if int(opcao) == 1:
        print(f"o seu saldo é R${SALDO}")

    #SAQUE
    elif int(opcao) == 2:
        
        saque = float(input("Digite o valor que deseja sacar: R$"))
        LIMITE_SAQUES = LIMITE_SAQUES - 1

        if saque <= SALDO and saque <= 500 and LIMITE_SAQUES >= 0:
            SALDO = SALDO - saque
            print(f"O valor de R${saque} foi sacado com sucesso!")
            extrato.append(f"Saque de R${SALDO}")

        else:
            if saque >= 500:
                print("Não é póssivel sacar valores acima de R$500.00")
            elif saque >= SALDO:   
                print(f"Saldo insuficiente R${SALDO}")
            else:
                print("Limite de saque diário atingido!")    
    
    #DEPOSITO
    elif int(opcao) == 3:
        deposito = float(input("Digite o valor que deseja depositar: R$"))
        if deposito > 0:
            SALDO = deposito + SALDO
            print(f"O valor de R${SALDO} foi depósitado com sucesso!")
            extrato.append(f"Depósito de R${SALDO}")

        else:
            print("Valor incorreto!")
            
    #EXTRATO
    elif int(opcao) == 4:
        print("\n --------------- EXTRATO ---------------")
        if extrato is not None:
            print(str(extrato).replace("'", ""))
            print(f"O seu saldo atual é R${SALDO}")
            print("---------------------------------------------")
        else:
            print("Não há registros de transações!")
            

    elif int(opcao) == 5:
        print("Obrigado pela preferência!")
        break

    else:
        print("Opção inválida, selecione novamente!\n")
    
