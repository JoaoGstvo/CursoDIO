import os


def depositar(saldo):
    deposito = float(input("Informe o valor a ser depositado: "))
    extrato = ""
    if deposito > 0:
        saldo += deposito
        extrato = f"Depósito de R${deposito:.2f}"
        print(f"Depósito realizado com sucesso! Saldo atual: {saldo}")
    else:
        print("Valor inválido. Por favor, insira um valor positivo.")

    return saldo, extrato



def sacar(saldo):
    LIMITE_VALOR = 500
    extrato = ""
    saque = float(input("Informe o valor a ser sacado: "))

    if saque > float(0) and saque <= LIMITE_VALOR and saque <= saldo:
        saldo -= saque
        extrato = f"Saque de R${saque:.2f}"
        print(f"Saque realizado com sucesso! Seu saldo atual é de: {saldo}")
    else:
        print("Saque não autorizado. Por favor, verifique o valor ou o se seu limite diário ja foi alcançado!")

    return saldo, extrato



def ver_extrato(extrato):
    print("⊰᯽⊱┈──╌♤ EXTRATO ♤╌──┈⊰᯽⊱")
    if extrato == []:
        print("Nenhum movimento realizado.")
    for i in range(len(extrato)):
        print(extrato[i])

    return extrato



saldo = 0
extrato = []
LIMITE_DIARIO = 3
i= 0

while True:



    menu = f"""
        ⊰᯽⊱┈──╌♤ MENU ♤╌──┈⊰᯽⊱
        Saldo: R${saldo:.2f}
        [d]Depositar
        [s]Sacar
        [e]Extrato
        [q]Sair
        => """
    print(menu)
        
    opcao = input("Opção: ")

    match opcao:
        case "d":
            os.system('cls')
            saldo, extrato_atual = depositar(saldo)
            extrato.append(extrato_atual)

        case "s":    
            os.system('cls')
            if i == LIMITE_DIARIO:  
                print("Limite diário de saques alcançado!")
            else:
                i +=  1
                saldo, extrato_atual = sacar(saldo)
                extrato.append(extrato_atual)

        case "e":
            os.system('cls')
            ver_extrato(extrato)

        case "q":
            os.system('cls')
            print("Saindo...")
            break

        case _:
            os.system('cls') 
            print("Opção inválida burro!")
           










