print("    ***BEM VINDO AO BANCO RAPOSÃO***       ")

def Usuario(usuarios):
    cpf = input("Informe o cpf (apenas números): ")
    usuario = Listar_usuarios(cpf, usuarios)
    
    if usuario:
        print("O CPF já está cadastrado!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, num. - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome,"data_nascimento": data_nascimento, "cpf": cpf,"endereco": endereco})
    
    print("Usuário criado com sucesso!")

def Listar_usuarios(cpf, usuarios):
    usuarios_filtrados  = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def Criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf (apenas números): ")
    usuario = Listar_usuarios(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, tente novamente")
    
def Listar_contas(contas):
    for conta in contas:
        print(f"""---------------------------------------------
                  Agência: {conta["agencia"]}
                  Conta Corrente: {conta["numero_conta"]}
                  Titular:{conta["usuario"]["nome"]}  
              """)
        print("---------------------------------------------")
    pass

def Deposito(valor_deposito, saldo, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito de R${valor_deposito:.2f}\n"
        print(f"O valor de R${valor_deposito:.2f} foi depósitado com sucesso!")        
    else:
        print("Valor incorreto!")

    return saldo, extrato

def Saque(*,valor_saque, saldo, extrato, valor_limite, numero_saque, limite_saque):    
    if valor_saque <= saldo and valor_saque <= valor_limite and numero_saque < limite_saque:            
        numero_saque += 1        
        saldo -= valor_saque
        extrato += f"Saque de R${valor_saque:.2f}\n" 
        print(f"O valor de R${valor_saque:.2f} foi sacado com sucesso!")
    else:
        if valor_saque > valor_limite:
            print("Não é póssivel sacar valores acima de R$500.00")
        elif valor_saque > saldo:   
            print(f"Saldo insuficiente R${saldo}")                        
        elif numero_saque >= limite_saque:
            print("Limite de saque diário atingido!")

    return saldo, extrato, numero_saque
    
def Extrato(saldo, /, *, extrato):
    print("\n --------------- EXTRATO ---------------")
    if extrato is not None:
        print(extrato.replace("'", ""))
        print("---------------------------------------------")
        print(f"O seu saldo atual é R${saldo:.2f}")
        print("---------------------------------------------")
    else:
        print("Não há registros de transações!")
 
def main():
    LIMITE_SAQUE = 3 
    AGENCIA = "0001"
    
    numero_saque = 0
    saldo = 0
    valor_limite = 500
    extrato = ""
    usuarios = []
    contas = []
    numero_conta = 0
    
    menu ="""
    --Selecione a opção desejada-----
                1 - Depósito
                2 - Saque
                3 - Extrato 
                4 - Novo Usuário
                5 - Nova Conta
                6 - Listar Contas
                7 - Sair
    ----------------------------------

                """
    while True:
        opcao = input(menu)      
        #DEPOSITO
        if int(opcao) == 1:
            valor_deposito = float(input("Digite o valor que deseja depositar: R$"))
            saldo, extrato = Deposito(valor_deposito, saldo, extrato)

        #SAQUE
        elif int(opcao) == 2:
            valor_saque = float(input("Digite o valor que deseja sacar: R$"))
            saldo, extrato, numero_saque = Saque(valor_saque=valor_saque,
                                   saldo=saldo,extrato=extrato,
                                   valor_limite=valor_limite,
                                   numero_saque=numero_saque,
                                   limite_saque=LIMITE_SAQUE)
            
        #EXTRATO
        elif int(opcao) == 3:        
            Extrato(saldo, extrato=extrato)
        
        #N. Usuário    
        elif int(opcao) == 4:
            Usuario(usuarios)
                 
        #N. Conta
        elif int(opcao) == 5:
            conta = Criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                numero_conta += 1
     
        #Listar Contas
        elif int(opcao) == 6:
            Listar_contas(contas)
                    
        elif int(opcao) == 7:
            print("Obrigado pela preferência!")
            break

        else:
            print("Opção inválida, selecione novamente!\n")
        
main()