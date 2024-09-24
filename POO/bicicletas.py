
class Bicicletas:

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def toString(self):
        return f"Cor: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano} Valor: {self.valor}"

    def buzinar(self):
        return("BIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")

    def parar(self):
        return("Parando..........")

    def acelerar(self):
        return("Vamo corre galeraaaa..........")
    

quantidade = int(input("Quantas bikes serão: "))
lista_bike = []
for i in range(quantidade):
    bike = Bicicletas(input("Cor: "), input("Modelo: "), int(input("Ano: ")), int(input("Valor: ")))
    lista_bike.append(bike)
    
for i in range(len(lista_bike)):
    print(lista_bike[i].toString())

print(lista_bike[0].acelerar())
print(lista_bike[0].parar())
print(lista_bike[0].buzinar())
