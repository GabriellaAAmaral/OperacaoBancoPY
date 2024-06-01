menu = """

====== MENU ========

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

====================

"""

saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input (menu)

    if opcao == "0":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print ("Operação falhou! O valor informado é inválido")


    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite 

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! O limite de saques foi excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido!")

    
    elif opcao == "2":
        print("\n============== EXTRATO ==============")
        print ("não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")

    elif opcao == "3":
        break
    
    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada!")