def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def main():
    # Solicita ao usuário que insira seu peso e altura
    peso = float(input("Digite o seu peso em quilogramas: "))
    altura = float(input("Digite a sua altura em metros: "))

    # Calcula o IMC usando a função calcular_imc
    imc = calcular_imc(peso, altura)

    # Exibe o resultado ao usuário
    print("Seu IMC é: {:.2f}".format(imc))

    # Verifica a faixa de IMC e fornece uma recomendação
    if imc < 18.5:
        print("Você está abaixo do peso normal.")
    elif imc < 25:
        print("Seu peso está dentro da faixa saudável.")
    elif imc < 30:
        print("Você está com sobrepeso.")
    else:
        print("Você está obeso.")

if __name__ == "__main__":
    main()

