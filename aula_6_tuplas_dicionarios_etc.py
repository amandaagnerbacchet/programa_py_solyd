#  Uma lista em Python é uma coleção ordenada e mutável de elementos.

#  Para criar uma lista, você pode colocar elementos entre colchetes [], 
#  separados por vírgulas. 
lista = [1, 2, 3, "abc"]


#  você pode alterar seus elementos depois de criá-las.

# Adicionando um elemento ao final da lista
lista.append(4)

# Removendo um elemento específico da lista
lista.remove(2)

# Modificando um elemento da lista
lista[0] = "xyz"



#  Você pode acessar os elementos de uma lista usando índices
# Acessando um elemento da lista
primeiro_elemento = lista[0]

# Slicing para acessar parte da lista
parte_da_lista = lista[1:3]



#   Python fornece uma variedade de métodos embutidos úteis para manipulação de listas
# Exemplo de uso de alguns métodos de lista
lista.append(5)     # Adiciona um elemento ao final da lista
lista.remove(3)     # Remove o primeiro elemento com o valor 3
lista.pop(0)        # Remove e retorna o elemento do índice 0
lista.insert(1, 10) # Insere o valor 10 no índice 1
lista.sort()        # Ordena os elementos da lista





#  Uma tupla em Python é uma coleção ordenada e imutável de elementos. 

#  A sintaxe básica para criar uma tupla é colocar os elementos entre parênteses ()
#  separados por vírgulas.
tupla = (1, 2, 3, "abc")
"""
As tuplas são úteis quando você deseja armazenar um conjunto de valores que não devem 
ser alterados, como coordenadas (x, y) em um plano cartesiano
"""




#  Você pode acessar os elementos de uma tupla usando índices
tupla = (1, 2, 3)
primeiro_elemento = tupla[0]  # Retorna 1



#  As tuplas também suportam slicing (fatiamento) para acessar partes da tupla:
tupla = (1, 2, 3, 4, 5)
parte_da_tupla = tupla[1:3]  # Retorna (2, 3)
"""
Embora as tuplas sejam imutáveis, você pode concatená-las, criar novas tuplas 
a partir de operações com outras tuplas e desempacotar tuplas.
"""







"""
Um dicionário em Python é uma coleção não ordenada de pares de chave-valor. 
Cada elemento no dicionário consiste em uma chave única e seu valor correspondente. 
Dicionários são extremamente flexíveis e úteis para armazenar e manipular dados em Python.
"""

#  Para criar um dicionário em Python, você usa chaves {}
dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}


# As chaves em um dicionário devem ser únicas. 
# Se você tentar adicionar uma chave que já existe, o valor correspondente será atualizado.
dicionario["idade"] = 31  # Atualiza o valor da chave "idade" para 31


#  Você pode acessar os valores de um dicionário usando suas chaves. 
# Se uma chave não existir no dicionário, isso resultará em um erro KeyError
print(dicionario["nome"])     # Saída: João
print(dicionario.get("idade"))# Saída: 31 (ou o valor correspondente)


#  Dicionários são mutáveis, o que significa que você pode adicionar,
#  modificar e remover elementos após a criação do dicionário.
dicionario["profissao"] = "Engenheiro"  # Adiciona uma nova chave-valor ao dicionário
del dicionario["cidade"]                # Remove a chave "cidade" e seu valor do dicionário



#  ython fornece uma variedade de métodos embutidos úteis para manipulação de dicionários
print(dicionario.keys())   # Retorna uma lista das chaves no dicionário
print(dicionario.values()) # Retorna uma lista dos valores no dicionário
print(dicionario.items())  # Retorna uma lista de tuplas (chave, valor) no dicionário
