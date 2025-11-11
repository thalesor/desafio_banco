def cadastrar_usuario(nome_usuario, nascimento_usuario, cpf_usuario, endereco_usuario, lista_usuarios):

    novo_usuario = {
        "nome": nome_usuario,
        "data_nascimento": nascimento_usuario,
        "cpf": cpf_usuario,
        "endereco": endereco_usuario
    }

    lista_usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso.")
    return lista_usuarios


def validar_cpf_existente(cpf_usuario, lista_usuarios):
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf_usuario:
            return False
        
    return True


def validar_conta_existente(numero_conta, lista_contas):
    for conta in lista_contas:
        if conta["numero"] == numero_conta:
            return True
        
    return False

def encontrar_conta_por_numero(numero_conta, lista_contas):
    # aceita "1" ou "0001" como entrada e transforma em "0001"
    numero_formatado = "%04d" % int(numero_conta)
    for conta in lista_contas:
        if conta.get("numero") == numero_formatado:
            return conta
    return None

def cadastrar_conta(agencia_conta, cpf_conta, lista_contas):
    if not validar_cpf_existente(cpf_conta, clientes):
        novo_numero = gerar_numero_conta(lista_contas)

        nova_conta = {
            "agencia": agencia_conta,
            "numero": novo_numero,
            "cpf": cpf_conta,
            "numero_saques": numero_saques,
            "saldo": 0,
            "extrato": "",
            "limite": limite,
            "limite_saques": LIMITE_SAQUES
        }

        lista_contas.append(nova_conta)
        print("Conta criada com sucesso.")
        return lista_contas

    print("Cliente não encontrado. Por favor, cadastre o usuário antes de criar uma conta.")

def gerar_numero_conta(lista_contas):
    novo = len(lista_contas) + 1
    return "%04d" % novo

def saque(*, saldo_conta, valor_saque, extrato_conta, limite_conta, num_saques, limite_saques):
    
    excedeu_saldo = valor_saque > saldo_conta

    excedeu_limite = valor_saque > limite_conta

    excedeu_saques = num_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    
    elif valor_saque > 0:
        saldo_conta -= valor
        extrato_conta += f"Saque: R$ {valor_saque:.2f}\n"
        num_saques += 1
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo_conta, extrato_conta, num_saques


def depositar(saldo_conta, valor_deposito, extrato_conta):
    
    if valor_deposito > 0:
        saldo_conta += valor_deposito
        extrato_conta += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo_conta, extrato_conta


def imprimir_extrato(extrato_conta, /, saldo_conta):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_conta else extrato_conta)
    print(f"\nSaldo: R$ {saldo_conta:.2f}")
    print("==========================================")


menu = """
[u] Cadastrar Usuario(Cliente)
[c] Cadastrar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
NUMERO_AGENCIA = "0001"
clientes = []
contas = []

while True:

    opcao = input(menu)

    if opcao == "d":

        num_conta = input("Informe o numero da conta: ")

        if not validar_conta_existente(num_conta, contas):
            print("Conta não encontrada. Por favor, cadastre uma conta antes de realizar saques.")
            continue

        conta = encontrar_conta_por_numero(num_conta, contas)

        valor = float(input("Informe o valor do depósito: "))
        conta["saldo"], conta["extrato"] = depositar(conta["saldo"], valor, conta["extrato"])


    elif opcao == "s":
        
        num_conta = input("Informe o numero da conta: ")

        if not validar_conta_existente(num_conta, contas):
            print("Conta não encontrada. Por favor, cadastre uma conta antes de realizar saques.")
            continue
        
        conta = encontrar_conta_por_numero(num_conta, contas)

        valor = float(input("Informe o valor do saque: "))
        conta["saldo"], conta["extrato"], conta["numero_saques"] = saque(saldo_conta=conta["saldo"], valor_saque=valor, extrato_conta=conta["extrato"], limite_conta=conta["limite"], num_saques=conta["numero_saques"], limite_saques=conta["limite_saques"])


    elif opcao == "e":
        
        num_conta = input("Informe o numero da conta: ")

        if not validar_conta_existente(num_conta, contas):
            print("Conta não encontrada. Por favor, cadastre uma conta antes de realizar saques.")
            continue

        conta = encontrar_conta_por_numero(num_conta, contas)

        imprimir_extrato(conta["extrato"], saldo_conta = conta["saldo"])


    elif opcao == "u":
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (DD-MM-AAAA): ")
        cpf = input("Informe o CPF (somente números): ")

        while not validar_cpf_existente(cpf, clientes):
            print("CPF já cadastrado! Por favor, informe um CPF válido.")
            cpf = input("Informe o CPF (somente números): ")

        endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
        
        clientes = cadastrar_usuario(nome, data_nascimento, cpf, endereco, clientes)


    elif opcao == "c":
        cpf = input("Informe o CPF do cliente: ")

        cliente_encontrado = False
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                cliente_encontrado = True
                break

        if cliente_encontrado:
            agencia = "0001"
            contas = cadastrar_conta(agencia, cpf, contas)
        else:
            print("Cliente não encontrado. Por favor, cadastre o usuário antes de criar uma conta.")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")