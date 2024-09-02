import os
import re

class Conta:
    def __init__(self, id, nome, senha, saldo, extrato):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.saldo = saldo
        self.extrato = extrato

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome
    
    def getSenha(self):
        return self.senha
    
    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self, saldo):
        self.saldo = saldo
    
    def getExtrato(self):
        return self.extrato
    
    def setExtrato(self, extrato):
        self.extrato = extrato

    def exibirInf(self):
        return f"Id: {self.id}\nNome: {self.nome}\nSenha: {self.senha}\nSaldo: {self.saldo}\nExtrato: {self.extrato}"
    
def cadastrarConta(contas, id_contador):
    print("\n##### Cadastre sua Conta #####\n")
    id = id_contador
    
    nome = input("Digite o nome de usuário: ").upper()
    if nome == "":
        print("\nNome de usuário não pode ser vazio!")
        return None
    elif nome in [conta.getNome().upper() for conta in contas]:
        print("\nNome de usuário já existe!")
        return None
    elif nome[0].isdigit():
        print("\nNome de usuário não pode começar com número!")
        return None
    elif not nome[0].isalpha():
        print("\nNome de usuário deve começar com letra!")
        return None
    elif re.match(".*[^A-Za-z0-9].*", nome):
        print("\nNome não deve ter caracteres especiais.")
        return None
    elif len(nome) < 3 or len(nome) > 20:
        print("\nNome de usuário deve ter entre 3 e 20 caracteres!")
        return None
    novoNome = nome.replace(" ","")
    
    nome = novoNome

    senha = input("Digite a senha: ")
    if senha == "":
        print("\nSenha não pode ser vazia!")
        return None
    elif len(senha) < 4:
        print("\nSenha deve conter no mínimo 4 caracteres!")
        return None
    
    saldo = 0
    extrato = []

    novaConta = Conta(id, nome, senha, saldo, extrato)
    contas.append(novaConta)

    print("\nCadastro Realizado com Sucesso!")


def entrarConta(contas):
    if contas != []:
        print("\n##### Entre na sua Conta #####\n")
        nome = input("Digite o nome de usuário: ").upper()
        if nome == "":
            os.system("cls")
            return
        senha = input("Digite a senha: ")

        for conta in contas:
            if conta.getNome().upper() == nome and conta.getSenha() == senha:
                print("\nBem-vindo, " + nome + "!")
                return conta
            
        print("\nNome ou senha incorretos! Tente novamente.")
    else:
        print("\nNenhuma conta cadastrada!")

    return None




def depositar(saldo):
    deposito = float(input("\nDigite o valor para depositar: "))
    extrato = "Inválido!"
    if deposito > 0:
        saldo += deposito
        extrato = "Depóstido de " + (f"R${deposito:,.2f}")
        print(f"\nDepósito realizado com sucesso!")
    else:
        print("\nValor inválido. Por favor, tente novamente.")

    return saldo, extrato


def sacar(saldo):
    LIMITE_SAQUE = 500
    extrato = "Inválido!"
    if saldo < 0:
        print("\nSaldo insuficiente. Por favor, tente novamente.")
    else:
        saque = float(input("\nDigite o valor para sacar: "))
        if saque > LIMITE_SAQUE:
            print("\nValor de saque excede o limite de R$500,00. Saque não realizado!")
        elif saque > saldo or saque <= 0:
            print("\nValor Inválido. Saque não realizado!")
        else:
            saldo -= saque
            extrato = "Saque de " + (f"R${saque:,.2f}")
            print(f"\nSaque realizado com sucesso!")
            return saldo, extrato
        
    return saldo, extrato

def transferir(contaLogada, contas):
    extrato = "Inválido!"
    saldo = contaLogada.getSaldo()

    if saldo > 0:
        try:
            status = False
            propriaConta = False
            print("\n##### Tranferência #####\n")
            id = int(input("Digite Id para transferir: "))
            for conta in contas:
                if id == conta.getId():
                    if contaLogada.getId() == conta.getId():
                        propriaConta = True
                    else:
                        status = True
                        valor = float(input("\nDigite o valor para transferir: "))       
                        saldoConta = conta.getSaldo()
                        extratoConta = conta.getExtrato()
                        if valor > 0:
                            novoValor = saldoConta + valor
                            conta.setSaldo(novoValor)
                            extratoConta.append(f"Recebeu R${valor:,.2f} de {contaLogada.getNome()}")
                            conta.setExtrato(extratoConta)

                            saldo -= valor
                            extrato = f"Enviou R${valor:,.2f} para {conta.getNome()}"

                        else:
                            print("\nValor Inválido!")
                            break

            if status:
                print("\nTransferência concluída com sucesso!")
            elif propriaConta:
                print("\nVocê não pode transferir para si mesmo!")
            else:
                print("\nConta não encontrada! Tente novamente.")
        except:
            print("\nId inválido. Por favor, tente novamente.")
    
    else:
        print("\nSaldo insuficiente. Por favor, tente novamente.")

    return saldo, extrato

                
def verExtrato(extrato):

    print("\n############## EXTRATO ##############\n")
    if extrato == []:
        print("Não há extrato disponível.")
    else:
        for i in range(len(extrato)):
            print(extrato[i])
    print("\n#####################################")


def verContas(contas):
    print("\n############## CONTAS ##############")
    if contas != []:
        for conta in contas:
            print(f"\n{conta.exibirInf()}")
    else:
        print("\nNenhuma conta registrada!")
    print("\n#####################################")

def menuConta(contaLogada, contas):

    nome = contaLogada.getNome()
    saldo = contaLogada.getSaldo()
    extrato = contaLogada.getExtrato()

    while True:

        menu = f"\n======= Conta Logada: {nome} =======\nSaldo = R${saldo:,.2f}\n\n[1] Depositar\n[2] Sacar\n[3] Transferir \n[4] Extrato \n[5] Sair \n"
        print(menu)
        escolha = input("Opção: ")

        match escolha:
            case "1":
                os.system("cls")
                deposito = depositar(saldo=saldo)
                if deposito[1] != "Inválido!":
                    saldo = deposito[0]
                    contaLogada.setSaldo(saldo)
                    extrato.append(deposito[1])
                    contaLogada.setExtrato(extrato)
            case "2":
                os.system("cls")
                saque = sacar(saldo=saldo)
                if saque[1] != "Inválido!":
                    saldo = saque[0]
                    contaLogada.setSaldo(saldo)
                    extrato.append(saque[1])
                    contaLogada.setExtrato(extrato)
            case "3":
                os.system("cls")
                transferencia = transferir(contaLogada, contas)
                if transferencia[1] != "Inválido!":
                    saldo = transferencia[0]
                    contaLogada.setSaldo(saldo)
                    extrato.append(transferencia[1])
                    contaLogada.setExtrato(extrato)
            case "4":
                os.system("cls")
                verExtrato(extrato=extrato)
            case "5":
                os.system("cls")
                break
            case _:
                os.system("cls")
                print("\nOpção inválida. Tente novamente.")

def telaInicial():
    contas = []
    conta1 = Conta(0,"DIGO", "1234", 100, [])
    conta2 = Conta(1,"JOHN", "1234", 0, [])
    contas.append(conta1)
    contas.append(conta2)

    id_contador = 2

    while True:
        print("\n##### Bem-vindo ao Sistema Bancário! #####\n")

        menu = f"[1] Cadastrar\n[2] Entrar\n[3] Sair\n\n[6] Ver Contas\n"
        print(menu)
        escolha = input("Opção: ")

        match escolha:
                case "1":
                    os.system("cls")
                    cadastro = cadastrarConta(contas, id_contador)
                    if cadastro != None:
                        id_contador += 1
                case "2":
                    os.system("cls")
                    login = entrarConta(contas)
                    if login != None:
                        os.system("cls")
                        menuConta(contaLogada=login, contas=contas)
                case "3":
                    print("\nSaindo...")
                    break
                case "6":
                    os.system("cls")
                    verContas(contas)
                case _:
                    os.system("cls")
                    print("\nOpção inválida. Tente novamente.")

telaInicial()