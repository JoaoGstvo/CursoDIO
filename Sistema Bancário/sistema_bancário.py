import os

def depositar(saldo):
    deposito = float(input("Informe o valor a ser depositado: "))
    extrato = ""
    if deposito >= 1:
        saldo += deposito
        extrato = f"Depósito de R${deposito:.2f}"
        print(f"Depósito realizado com sucesso! Saldo atual: {saldo}")
    else:
        print("Valor inválido. Por favor, insira um valor maior que 1.")

    return saldo, extrato



def sacar(saldo):
    LIMITE_VALOR = 500
    extrato = ""
    saque = float(input("Informe o valor a ser sacado: "))

    if saque >= float(1) and saque <= LIMITE_VALOR and saque <= saldo:
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


def criar_conta(identificador_conta):
    conta = {
        "id": identificador_conta,
        "nome": input("Digite seu nome: "),
        "senha": input("Crie sua senha (Apenas letras): "),
    }
    return conta


saldo = 0
extrato = []
contas = {}
i= 0
identificador_conta = 0
LIMITE_DIARIO = 3
SENHA_ADM = "ADM"

menu_adm = f"""
        ⊰᯽⊱┈──╌♤ MENU ADM ♤╌──┈⊰᯽⊱

        [a]Visualizar Contas
        [b]Remover Conta
        => """

menu = f"""
    ⊰᯽⊱┈──╌♤ MENU ♤╌──┈⊰᯽⊱
    Saldo: R${saldo:.2f}
    [a]Criar Conta
    [d]Depositar
    [s]Sacar
    [e]Extrato
    [q]Sair
    [r]ADM
    => """

while True:
    
    print(menu)

    opcao = input("Opção: ")

    match opcao:

        case "a":
            os.system('cls')
            identificador_conta += 1
            nova_conta = criar_conta(identificador_conta)
            contas.update(nova_conta)
            print("Conta criada com sucesso!")
            
        case "r":
            os.system('cls')
            senha = input("Digite a senha: ")

            if senha == SENHA_ADM:
                os.system('cls')
                
                print(menu_adm)
                opcao_adm = input("Opção: ")

                match opcao_adm:
                    case "a":
                        os.system('cls')
                        print(contas.values())
                    # case "b":
                    #     print()
        
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
           

    








