print("programa de controle de festas")

nunber_convid = input("digite o numero de convidados \n")


lista_de_convidados = []

i = 1
while i <= int(nunber_convid):
    nome_convidado = input("qual o nome do convidado?" + str(i) + ":" )
    lista_de_convidados.append(nome_convidado)
    i += 1

print('\n temos', nunber_convid, 'convidados')
# uma outra forma de fazer isso é 
print( f"Temos: {nunber_convid}, convidados")
print( f"Os convidados são: {nome_convidado}.")


for convite in lista_de_convidados:
    print(convite)
    print("\n boas festas")
