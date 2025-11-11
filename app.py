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

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo_conta, extrato_conta, num_saques

def depositar(saldo_conta, valor_deposito, extrato_conta):
    
    if valor_deposito > 0:
        saldo_conta += valor_deposito
        extrato_conta += f"Depósito: R$ {valor_deposito:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo_conta, extrato_conta

def imprimir_extrato(extrato_conta, /, saldo_conta):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_conta else extrato_conta)
    print(f"\nSaldo: R$ {saldo_conta:.2f}")
    print("==========================================")



menu = """

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

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(saldo_conta=saldo, valor_saque=valor, extrato_conta=extrato, limite_conta=limite, num_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        imprimir_extrato(extrato, saldo_conta=saldo)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada, ou selecione 0 para voltar ao menu anterior")