# 01. Implementar uma função que escreva no terminal os números naturais de 1 até um número informado.
# Ex: (10) => 1 2 3 4 5 6 7 8 9 10

# number = int(input())
# for i in range(number):
#     print(i, end=' ')

#-----------------------------------------------------------------------------------------------------------------------

# 02. Implementar uma função que escreva no terminal os números naturais pares de 0 até um número informado.
# Ex: (10) => 0 2 4 6 8 10

# numbers = int(input())
# for i in range(0, numbers, 2):
#     print(i, end=' ')

#-----------------------------------------------------------------------------------------------------------------------

# 03. Implementar uma função que escreva no terminal os números naturais ímpares de 1 até um número informado.
# Ex: (10) => 1 3 5 7 9

# numbers = int(input())
# for i in range(numbers):
#     if i % 2 != 1:
#         print(i, end=' ')

#-----------------------------------------------------------------------------------------------------------------------

# 04. Implementar uma função que escreva no terminal os números naturais, a partir de um número de início e fim.
# Ex: (3, 11) => 3 4 5 6 7 8 9 10 11

# def naturais_crescente():
#     first_number = int(input())
#     second_number = int(input())
#     i = first_number
#     print()
#     while i <= second_number:
#         i+=1
#         print(i-1)
#         if first_number == second_number:
#             break

# naturais_crescente()    

#-----------------------------------------------------------------------------------------------------------------------

# 05. Implementar uma função que escreva no terminal os números naturais de 1 até um número informado de forma decrescente.
# Ex: (10) => 10 9 8 7 6 5 4 3 2 1



#-----------------------------------------------------------------------------------------------------------------------

# 06. Implementar uma função que escreva no terminal os números naturais pares de 0 até um número informado de forma decrescente.
# Ex: (10) => 10 8 6 4 2 0

# def pares_decrescente():
#     number = int(input())
#     print()
#     for i in range(number, - 1, -1):
#         if i % 2 == 0:
#             print(i, end=' ')

# pares_decrescente()

#-----------------------------------------------------------------------------------------------------------------------

# 07. Implementar uma função que escreva no terminal os números naturais ímpares de 1 até um número informado de forma decrescente.
# Ex: (10) => 9 7 5 3 1

# def impares_decrescente():
#     number = int(input())
#     print()
#     for i in range(number, - 1, -1):
#         if i % 2 !=0:
#             print(i, end=' ')

# impares_decrescente()

#-----------------------------------------------------------------------------------------------------------------------

# 08. Implementar uma função que escreva no terminal os números naturais, a partir de um número de início e fim, de forma decrescente.
# Ex: (3, 11) => 11 10 9 8 7 6 5 4 3

# def naturais_decrescente():
#     first_number = int(input())
#     second_number = int(input())
#     i = max(first_number, second_number)
#     print()
#     while i >= min(first_number, second_number):
#         i-=1
#         print(i+1)

# naturais_decrescente()

#-----------------------------------------------------------------------------------------------------------------------

# 09. Implementar uma função que escreva no terminal os números naturais múltiplos de número informado, de 0 até outro número informado.
# Ex1: (4, 20) => 0, 4, 8, 12, 16, 20

# def multiplos():
#     first_number = int(input())
#     second_number = int(input())
#     i = min(first_number, second_number)
#     print()

#     while i <= max(first_number, second_number):
#         i += min(first_number, second_number)
#         print(i - min(first_number, second_number))

# multiplos()

#-----------------------------------------------------------------------------------------------------------------------

# 10. Implementar uma função que escreva no terminal o dobro dos números naturais de 1 até um número informado. A mensagem deve estar no formato: "O dobro de X é Y".
# Ex:  (5) => O dobro de 1 é 2
#             O dobro de 2 é 4
#             O dobro de 3 é 6
#             O dobro de 4 é 8
#             O dobro de 5 é 10

# def dobro():
#     number = int(input())
#     i = 1
#     print()
#     while i <= number:
#         print(f'O dobro de {i} é {i*2}')
#         i += 1

# dobro()

#-----------------------------------------------------------------------------------------------------------------------

# 11. Implementar uma função que escreva no terminal a tabuada de um número informado. A mensagem deve estar no formato: "A x B = X".
# Ex:  (5) => 5 x 1 = 5
#             5 x 2 = 10
#             5 x 3 = 15
#             5 x 4 = 20
#             5 x 5 = 25
#             5 x 6 = 30
#             5 x 7 = 35
#             5 x 8 = 40
#             5 x 9 = 45
#             5 x 10 = 50

# def tabuada():
#     number = int(input())
#     i = 1
#     while i <= 10:
#         print(f'{number} x {i} = {number * i}')
#         i += 1

# tabuada()

#-----------------------------------------------------------------------------------------------------------------------

# 12. Implementar uma função que retorne um texto que represente a forma de uma linha a partir do tamanho de pontos que a compõem, conforme abaixo:
# Exemplo: 4 pontos
# * * * *

# def desenhar():
#     pontos = int(input())
#     for i in range(pontos):
#         print("*", end=" ")

# desenhar()

#-----------------------------------------------------------------------------------------------------------------------

# 13. Implementar uma função que retorne um texto que represente a forma de um quadrado a partir da quantidade de linhas, conforme abaixo:
# Exemplo: 4 linhas
# * * * *
# * * * *
# * * * *
# * * * *

# def desenhar():
#     pontos = int(input())
#     for i in range(pontos):
#         print("* "*4)

# desenhar()

#-----------------------------------------------------------------------------------------------------------------------

# 14. Implementar uma função que retorne um texto que represente a forma de um retângulo a partir da quantidade de linhas e colunas, conforme abaixo:
# Exemplo: 4 linhas e 2 colunas
# * *
# * *
# * *
# * *

# def desenhar():
#     pontos = int(input())
#     for i in range(pontos):
#         print("* "*2)

# desenhar()

#-----------------------------------------------------------------------------------------------------------------------

# 15. Implementar uma função que retorne um texto que represente a forma de um triângulo a partir da quantidade de linhas, conforme abaixo:
# Exemplo: 5 linhas
# *
# * *
# * * *
# * * * * 
# * * * * *

# def desenhar():
#     pontos = int(input())
#     for i in range(1, pontos+1):
#         print('*' * i)

# desenhar()

#-----------------------------------------------------------------------------------------------------------------------

# 16. Implementar uma função que retorne um texto que represente a forma de um triângulo invertido a partir da quantidade de linhas, conforme abaixo:
# Exemplo: 5 linhas
#         *
#       * *
#     * * *
#   * * * * 
# * * * * *

# def desenhar():
#     pontos = int(input())
#     for i in range(1, pontos+1):
#         print( (' ' * pontos) + '*' * i)
#         pontos -=1
# desenhar()

#-----------------------------------------------------------------------------------------------------------------------

# 17. Implementar uma função que calcule a soma dos números naturais de 1 até um número informado.
# Ex: Somar de 1 até 5 => 1+2+3+4+5 => 15

# def somar():
#     numero = int(input(""))
#     soma = 0

#     for i in range(1, numero+1):
#         print (str(i) + '+', end='')
#         soma += i
#     print('=', soma)
# somar()

#-----------------------------------------------------------------------------------------------------------------------

# dqowdnoqndowqndoqw





















# def desenhar():
#     pontos = int(input())
#     for i in range(1, pontos+1):
#         print( (' ' * pontos) + '* ' * i)
#         pontos -=1
# desenhar()