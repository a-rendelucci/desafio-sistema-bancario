menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação realizada com sucesso.\n")
        else:
            print("Operação falhou! O valor informado é inválido.\n")    

    elif opcao == "2":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários alcançados.\n")
            menu = """

[1] Depositar
[3] Extrato 
[0] Sair

"""
        else:
            valor = float(input("Informe o valor do saque: "))
            if valor > 0:
                if valor <= limite:
                    if valor <= saldo:
                        saldo -= valor
                        numero_saques += 1
                        extrato += f"Saque: R$ {valor:.2f}\n"
                        print("Operação realizada com sucesso.\n")
                    else:
                        print(f"Não há saldo suficiente. Saldo disponível: R$ {saldo:.2f}\n")
                else:
                    print("Valor superior ao limite.\n")
            else:
                print("Operação falhou! O valor informado é inválido.\n")
       
    
    elif opcao == "3":
        print("Extrato\n")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}\n")

    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços.\n")
        break
    
    else:
        print("Operação inválida, por favor selecione a operação desejada.")