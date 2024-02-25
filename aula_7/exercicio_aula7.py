def encontrar_maior_menor(colecao):
    if not colecao:
        return None, None  # Retorna None para ambos maior e menor se a coleção estiver vazia
    
    maior = colecao[0]  # Assume que o primeiro elemento é o maior
    menor = colecao[0]  # Assume que o primeiro elemento é o menor
    
    for numero in colecao:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    
    return maior, menor

# Exemplo de uso da função
numeros = [10, 5, 20, 15, 8]
maior_numero, menor_numero = encontrar_maior_menor(numeros)
print("O maior número é:", maior_numero)
print("O menor número é:", menor_numero)
