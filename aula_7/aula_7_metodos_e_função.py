def somatorio_1_e_2(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def main():
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite o segundo número: "))
    
    # Chamando a função somatorio_1_e_2 para calcular o resultado
    resultado = somatorio_1_e_2(numero1, numero2)
    
    # Imprimindo o resultado dentro da função main
    print("O somatório é:", resultado)

# Chamando a função main para executar o código
main()
