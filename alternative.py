# Bhaskara
# import math
# def bhaskara():
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     delta = (b**2) - (4 * a * c)

#     if delta > 0:
#         raiz_positiva = (- (b) + math.sqrt(delta)) / (2 * a)
#         raiz_negativa = (- (b) - math.sqrt(delta)) / (2 * a)
#         print(f'x1 é igual a: {raiz_positiva}')
#         print(f'x2 é igual a: {raiz_negativa}')
#     else:
#         print("Delta resultou em um valor negativo, portanto, não é possível calcular as raízes!")

# bhaskara()


# lista = []
# selecao_par = []
# selecao_impar = []
# i = 0
# while i < 10:
#     lista.append(int(input()))
#     i+=1

# for i in lista:
#     if i % 2 ==0:
#         selecao_par.append(i)
#     else:
#         selecao_impar.append(i)    

# lista = [selecao_par, selecao_impar]
# print(lista)


def pode_ir_ao_cinema():

    preco_ingresso = 30.00
    preco_ubber = 30.00
    preco_comida = 20.00

    valor1 = float(input("Informe o valor que a primeira pessoa possui: "))
    valor2 = float(input("Informe o valor que a segunda pessoa possui: "))
    
    carona = input("Vão de carona? (Sim/Não): ").strip().lower() == "sim"
    comer = input("Vão comer no cinema? (Sim/Não): ").strip().lower() == "sim"
    vr = input("Possuem VR? (Sim/Não): ").strip().lower() == "sim"
    ganhou_ingressos = input("Ganharam os ingressos? (Sim/Não): ").strip().lower() == "sim"

    custo_ingresso = 0 if ganhou_ingressos else preco_ingresso * 2
    custo_transporte = 0 if carona else preco_ubber
    custo_comida = 0 if not comer else preco_comida * 2
    custo_total = custo_ingresso + custo_transporte + custo_comida

    if vr and comer:
        custo_total -= preco_comida * 2

    valor_total = valor1 + valor2

    if valor_total >= custo_total:
        print("Vai dar certo o cinema? true")
    else:
        print("Vai dar certo o cinema? false")

pode_ir_ao_cinema()

