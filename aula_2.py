idade = int(input("digite sua idade:"))

if idade < 18:
    print("acesso negado, voce é menor de idade")
elif idade > 59:
    print("acesso negado, é proibida a entrada de maiores de 60 anos")
else:
    print("acesso liberado")    