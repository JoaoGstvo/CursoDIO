# Constantes:
# Letra Maiúscula
# Ex: BRAZILIAN_STATES = ['Sp', 'Rj', 'Rs']

#-----------------------------------------------------------------------------------------------------------------------

# Conversão:
# Int -> Float
# age = 12
# age = float(age)
# print(age)

# Float -> Int
# price = 15.50
# price = int(price)
# print(price)

# Número -> Str
# number = 12
# number = str(number)
# print(number)
# Não podemos converter Str para Números, somente números para Str

#-----------------------------------------------------------------------------------------------------------------------

# Entrada de Dados
# variavel = input("Digite seu nome: ")
# print(variavel)

#-----------------------------------------------------------------------------------------------------------------------

# Atribuição com Adição     # Atribuição com Subtração      # Atribuição com Multiplição        # Atribuição com Divisão    ETC...
# number = 500              # number = 500                  # number = 500                      # number = 500
# number += 100             # number -= 100                 # number *= 100                     # number /= 100
# print(number)             # print(number)                 # print(number)                     # print(number)

#-----------------------------------------------------------------------------------------------------------------------

# Operadores Lógicos
# and = Só retorna True se as duas expressões forem Verdadeiras
# or  = Só retorna False se as duas expressões forem Falsas 
# Not = Ele sempre inverte o resultado das expressões, True == False e False == True

#-----------------------------------------------------------------------------------------------------------------------

# Operador de Identidade
# Utilizamos ele para saber se os valores das variáveis estão alocados no mesmo lugar da memória
# curso = 'Curso da DIO'
# nome_curso = curso
# print(curso is nome_curso)  [True]
# print(curso is not nome_curso) {Ou mudamos os valores das variáveis para que fiquem diferentes}  [False]

#-----------------------------------------------------------------------------------------------------------------------

# Operador de Associação
# Utilizamos ele para verificar se um elemento está presente em uma sequência
# course = 'Curso da DIO'
# fruits = ['Maça', 'Tomate', 'Banana']
# print('da' in course)
# print('Ferrugem' not in course)
# print('Ferrugem' in course)
# print('Maça' in fruits)
# print('Laranja' not in fruits)
# print('Laranja' in fruits)

#-----------------------------------------------------------------------------------------------------------------------

# Condições
#IF/ELIF/Else
# import sys
# option = int(input('Informe uma opção: [1] Sacar \n [2] Extrato: \n'))
# if option == 1:
#     valor = float(input('Informe o valor a ser sacado: '))
#     print('Sacou')
# elif option == 2:
#     print('Exibindo resultado')
# else:
#     sys.exit('Opção inválida')

# IF TERNÁRIO
# saque = 600
# saldo = 600
# status = 'Sucesso' if saque <= saldo else 'Falha'
# print(f'{status} ao realizar saque!')

#-----------------------------------------------------------------------------------------------------------------------
# Repetição FOR
# Exemplo utilizando um iterável
# texto = input("Informe um texto: ")
# VOGAIS = "AEIOU"
# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end="")
# else:
#     print()  # adiciona uma quebra de linha

# # Exemplo utilizando a função built-in range
# for numero in range(0, 51, 5):
#     print(numero, end=" ")

#   WHILE
# opcao = -1
# while opcao != 0:
#     opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

#     if opcao == 1:
#         print("Sacando...")
#     elif opcao == 2:
#         print("Exibindo o extrato...")
# else:
#     print("Obrigado por usar nosso sistema bancário, até logo!")


#     BREAK
# while True:
#     numero = int(input("Informe um número: "))
#     if numero == 10:
#         break

#     if numero % 2 == 0:
#         continue

#     print(numero)

#-----------------------------------------------------------------------------------------------------------------------

# Strings

# curso = "pYthon"
# print(curso.upper())
# print(curso.lower())
# print(curso.title())

# curso = "     Python "
# print(curso.strip())
# print(curso.lstrip())
# print(curso.rstrip())

# curso = "Python"
# print(curso.center(10, "#"))
# print(".".join(curso))


# Concatenação com formatação de casas decimais

# nome = "Guilherme"
# idade = 28
# profissao = "Progamador"
# linguagem = "Python"
# saldo = 45.435

# # print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
# print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")


# Fatiação de Strings

# nome = "João Gustavo do Carmo Moraes"
# print(nome[0])
# print(nome[-2])
# print(nome[:9])
# print(nome[10:])
# print(nome[10:16])
# print(nome[10:16:2])
# print(nome[:])
# print(nome[::-1])


# Strings Triplas

# nome = "João"
# mensagem = f"""
# Olá meu nome é {nome},
# Eu estou aprendendo Python.
# Essa mensagem tem diferentes recuos.
# """
# print(mensagem)

# print(
#     """
#     ============= MENU =============

#     1 - Depositar
#     2 - Sacar
#     0 - Sair

#     ================================

#     Obrigado por usar nosso sistema!!!!
# """
# )

#-----------------------------------------------------------------------------------------------------------------------

# Kwargs e *args

# def configurar_carro(**kwargs):
#     if 'cor' in kwargs:
#         print(f"Carro configurado com a cor: {kwargs['cor']}")
#     if 'modelo' in kwargs:
#         print(f"Modelo do carro: {kwargs['modelo']}")
#     if 'ano' in kwargs:
#         print(f"Ano do carro: {kwargs['ano']}")

# # Chamando a função com diferentes combinações de parâmetros
# configurar_carro(cor="Vermelho", modelo="SUV", ano=2022)


# def soma(*args):
#     return sum(args)

# print(soma(1, 2, 3))  # Saída: 6
# print(soma(10, 20))

#-----------------------------------------------------------------------------------------------------------------------

# Listas

# Criar uma lista
# minha_lista = [1, 2, 3, 4]

# # Adicionar elementos
# minha_lista.append(5)         # Adiciona ao final
# minha_lista.insert(1, 10)     # Adiciona na posição específica

# # Remover elementos
# minha_lista.remove(10)        # Remove o primeiro elemento encontrado
# minha_lista.pop(2)            # Remove o elemento no índice 2
# minha_lista.pop()             # Remove o último elemento
# minha_lista.clear()           # Remove todos os elementos

# # Acessar elementos
# valor = minha_lista[0]        # Acessa o primeiro elemento
# sub_lista = minha_lista[1:3]  # Acessa uma sublista (do índice 1 ao 2)

# # Verificar presença de um item
# if 3 in minha_lista:          
#     print("O número 3 está na lista")

# # Tamanho da lista
# tamanho = len(minha_lista)

# # Ordenar uma lista
# minha_lista.sort()            # Ordena em ordem crescente
# minha_lista.sort(reverse=True) # Ordena em ordem decrescente
# lista_ordenada = sorted(minha_lista)  # Retorna uma nova lista ordenada

# # Reverter a ordem da lista
# minha_lista.reverse()

# # Contar ocorrências de um item
# ocorrencias = minha_lista.count(2)

# # Encontrar o índice de um item
# indice = minha_lista.index(3)

# # Concatenar listas
# nova_lista = minha_lista + [6, 7, 8]

# # Repetir uma lista
# lista_repetida = minha_lista * 2

# # Copiar uma lista
# copia_lista = minha_lista.copy()

# # Compreensão de lista (List Comprehension)
# quadrados = [x**2 for x in minha_lista]

#-----------------------------------------------------------------------------------------------------------------------

# Conjuntos

# # Criar um conjunto (set)
# meu_set = {1, 2, 3, 4}

# # Adicionar elementos
# meu_set.add(5)               # Adiciona o elemento 5

# # Remover elementos
# meu_set.remove(2)            # Remove o elemento 2 (gera erro se não existir)
# meu_set.discard(3)           # Remove o elemento 3 (não gera erro se não existir)
# meu_set.pop()                # Remove e retorna um elemento arbitrário
# meu_set.clear()              # Remove todos os elementos

# # Verificar a presença de um item
# if 4 in meu_set:
#     print("O número 4 está no set")

# # Tamanho do conjunto
# tamanho = len(meu_set)

# # União de dois conjuntos
# outro_set = {3, 4, 5}
# uniao = meu_set.union(outro_set)  # Retorna a união dos conjuntos

# # Interseção de dois conjuntos
# intersecao = meu_set.intersection(outro_set)  # Retorna os elementos comuns

# # Diferença entre dois conjuntos
# diferenca = meu_set.difference(outro_set)  # Retorna os elementos que estão no meu_set, mas não no outro_set

# # Diferença simétrica entre dois conjuntos
# dif_simetrica = meu_set.symmetric_difference(outro_set)  # Retorna os elementos que estão em um set ou no outro, mas não em ambos

# # Atualizar o conjunto com outro conjunto
# meu_set.update(outro_set)  # Adiciona os elementos de outro_set ao meu_set

# # Atualizar com a interseção
# meu_set.intersection_update(outro_set)  # Mantém apenas os elementos presentes em ambos os conjuntos

# # Atualizar com a diferença
# meu_set.difference_update(outro_set)  # Remove os elementos de outro_set do meu_set

# # Atualizar com a diferença simétrica
# meu_set.symmetric_difference_update(outro_set)  # Mantém apenas os elementos que estão em um ou outro, mas não em ambos

# # Subconjunto e superconjunto
# is_subset = meu_set.issubset(outro_set)         # Verifica se meu_set é subconjunto de outro_set
# is_superset = meu_set.issuperset(outro_set)     # Verifica se meu_set é superconjunto de outro_set

# # Conjuntos disjuntos
# is_disjoint = meu_set.isdisjoint(outro_set)     # Verifica se os conjuntos não têm elementos em comum

# # Copiar um conjunto
# copia_set = meu_set.copy()

#-----------------------------------------------------------------------------------------------------------------------

# # Criar um dicionário
# meu_dict = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}

# # Adicionar ou atualizar elementos
# meu_dict['profissão'] = 'Engenheiro'  # Adiciona uma nova chave-valor
# meu_dict['idade'] = 26                # Atualiza o valor de uma chave existente

# # Remover elementos
# meu_dict.pop('cidade')                # Remove a chave 'cidade' e retorna o valor associado
# meu_dict.popitem()                    # Remove e retorna o último par chave-valor inserido
# del meu_dict['profissão']             # Remove a chave 'profissão'
# meu_dict.clear()                      # Remove todos os elementos do dicionário

# # Acessar elementos
# valor = meu_dict['nome']              # Acessa o valor associado à chave 'nome'
# valor = meu_dict.get('idade', 30)     # Retorna o valor de 'idade', ou 30 se não existir

# # Verificar a existência de uma chave
# if 'idade' in meu_dict:
#     print("A chave 'idade' está presente no dicionário")

# # Tamanho do dicionário
# tamanho = len(meu_dict)

# # Obter todas as chaves, valores ou itens (pares chave-valor)
# chaves = meu_dict.keys()              # Retorna todas as chaves
# valores = meu_dict.values()           # Retorna todos os valores
# itens = meu_dict.items()              # Retorna todos os pares chave-valor

# # Atualizar um dicionário com outro
# outro_dict = {'altura': 180, 'peso': 75}
# meu_dict.update(outro_dict)           # Atualiza meu_dict com os pares chave-valor de outro_dict

# # Iterar sobre o dicionário
# for chave, valor in meu_dict.items():
#     print(f'{chave}: {valor}')        # Itera sobre as chaves e valores

# # Copiar um dicionário
# copia_dict = meu_dict.copy()

# # Criar um dicionário com chaves padronizadas
# chaves_padrao = ['a', 'b', 'c']
# meu_dict = dict.fromkeys(chaves_padrao, 0)  # Cria um dicionário com todas as chaves tendo valor 0

# # Obter um valor com um valor padrão se a chave não existir
# valor = meu_dict.setdefault('nome', 'Desconhecido')  # Retorna o valor de 'nome', ou define 'Desconhecido' se não existir

#-----------------------------------------------------------------------------------------------------------------------

# from datetime import datetime, date, time, timedelta

# # Obter a data e hora atual
# agora = datetime.now()                 # Retorna a data e hora atuais
# hoje = date.today()                    # Retorna a data atual (somente a parte da data)

# # Criar um objeto de data
# minha_data = date(2024, 9, 12)         # Cria uma data específica (ano, mês, dia)

# # Criar um objeto de tempo
# meu_tempo = time(14, 30, 45)           # Cria um horário específico (hora, minuto, segundo)

# # Criar um objeto de data e hora
# minha_data_hora = datetime(2024, 9, 12, 14, 30, 45)  # Cria uma data e hora específicas

# # Extrair informações de uma data/hora
# ano = agora.year                       # Obtém o ano atual
# mes = agora.month                      # Obtém o mês atual
# dia = agora.day                        # Obtém o dia atual
# hora = agora.hour                      # Obtém a hora atual
# minuto = agora.minute                  # Obtém o minuto atual
# segundo = agora.second                 # Obtém o segundo atual

# # Formatar data/hora como string
# data_formatada = agora.strftime('%d/%m/%Y')         # Formata a data como 'dia/mês/ano'
# hora_formatada = agora.strftime('%H:%M:%S')         # Formata o horário como 'hora:minuto:segundo'

# # Converter string para data/hora
# data_convertida = datetime.strptime('12/09/2024', '%d/%m/%Y')  # Converte uma string para datetime

# # Trabalhar com diferenças de tempo (timedelta)
# delta = timedelta(days=10, hours=2)   # Define um intervalo de 10 dias e 2 horas
# nova_data = agora + delta              # Adiciona o intervalo à data/hora atual
# data_passada = agora - delta           # Subtrai o intervalo da data/hora atual

# # Calcular a diferença entre duas datas
# data1 = datetime(2024, 9, 12)
# data2 = datetime(2024, 10, 2)
# diferenca = data2 - data1              # Retorna a diferença como um timedelta

# # Comparar datas
# if data1 < data2:
#     print("data1 é anterior a data2")

# # Obter o timestamp atual
# timestamp = agora.timestamp()          # Retorna o timestamp atual (segundos desde 01/01/1970)

# # Converter timestamp para data/hora
# data_timestamp = datetime.fromtimestamp(timestamp)  # Converte o timestamp para datetime

# # Obter o dia da semana
# dia_semana = agora.weekday()           # Retorna o dia da semana (0 = segunda-feira, 6 = domingo)
# dia_semana_nome = agora.strftime('%A') # Retorna o nome do dia da semana (ex: 'Monday')

# # Adicionar ou subtrair horas/minutos/segundos
# nova_hora = agora + timedelta(hours=5)    # Adiciona 5 horas à data e hora atual
# nova_data = agora - timedelta(weeks=2)    # Subtrai 2 semanas da data e hora atual
