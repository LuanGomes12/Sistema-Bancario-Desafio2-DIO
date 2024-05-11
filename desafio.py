menu ="""
===== MENU =====
[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair
================
=>"""

saldo = 0
limite_maximo_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("deposito")
        deposito = float(input("Quanto você deseja depositar?"))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}"
            print("Operação realizada com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "2":
        print("saque")
        saque = float(input("Quanto você deseja sacar?"))

        if saque <= saldo:
            if saque <= limite_maximo_saque:
                numero_saques += 1
                if numero_saques <= LIMITE_SAQUES_DIARIOS:
                    saldo -= saque
                    extrato += f"Saque: R$ {saque:.2f}"
                    print("Operação realizada com sucesso!")
                else:
                    print("Número limite de saques diários antigido! Você só poderá sacar novamente em 24 horas!")
            else:
                print("Operação falhou! Valor informado excede o limite de saque diário (R$500,00 reais).")

        else:
            print("Operação falhou! Você não tem saldo suficiente.")   
    elif opcao == "3":
        print("\n==== EXTRATO ====")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(f"Saldo: R$ {saldo:.2f}")
        print("=================")
    elif opcao == "0":
        print("Obrigado por usar nossos serviços!")
        break
    else:
        print("Operação inválida! Digite novamente a operação desejada!")