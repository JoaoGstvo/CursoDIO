saldo = 2000 


def escolher_opcao():
    menu = """
        ================ MENU ================
        [d]Depositar
        [s]Sacar
        [e]Extrato
        [q]Sair
        => """
    escolha = input()
    print(menu)

escolher_opcao()



def depositar():
    global saldo
    deposito = float(input("Informe o valor a ser depositado: "))
    if deposito > 0:
        saldo += deposito
        print(f"Depósito realizado com sucesso! Saldo atual: {saldo}")
    else:
        print("Valor inválido. Por favor, insira um valor positivo.")

depositar()



def sacar():
    global saldo
    limite = 500
    saque = float(input("Informe o valor a ser sacado: "))
    if saque <= limite and saque <= saldo:
        saldo -= saque
        print(f"Saque realizado com sucesso! Seu saldo atual é de: {saldo}")
    else:
        print("Saque não autorizado. Por favor, verifique o valor ou o se seu limite diário ja foi alcançado!")

sacar()



def main():
    LIMITE_SAQUES = 3
    # saldo = 0
    # limite = 500
    # extrato = []

    while True:
        opcao = escolher_opcao()

        if opcao == "d":
            print("Depósito")
        
        elif opcao == "s":
            print("Sacar")

        elif opcao == "e":
            print("Extrato")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()





# def extrato():
#     print("extrato")
# depositar()



