arquivo = open('arquivoexenplo.txt', 'r' )

'''
open(): Esta função é usada para abrir um arquivo. 
O primeiro argumento é o nome do arquivo que você deseja abrir e o 
segundo argumento é o modo de abertura. 'r' 
indica que o arquivo está sendo aberto no modo de leitura (read).
''' 
conteudo = arquivo.read('arquivoexenplo.txt')
'''
read(): Este método lê todo o conteúdo do arquivo e o retorna como uma string.
''' 

linha = arquivo.readline('arquivoexenplo.txt')
'''
readline(): Este método lê uma linha do arquivo e a retorna como uma string. 
Ele lê até encontrar um caractere de nova linha (\n).
'''

arquivo.close('arquivoexenplo.txt')
'''
close(): Este método é usado para fechar o arquivo após a conclusão das operações de leitura ou escrita. 
É uma boa prática fechar o arquivo quando você terminar de trabalhar com ele para liberar recursos do sistema.
'''

for linha in arquivo:
    print(linha)