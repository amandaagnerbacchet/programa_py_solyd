from veiculo import Veiculo

caminhao_rosa = Veiculo('rosa', 6, 'ford')

print(type(caminhao_rosa.marca))
print(caminhao_rosa.marca, caminhao_rosa.cor, caminhao_rosa.rodas)

caminhao_azul = Veiculo('azul', 23, 'mercedez')

print(caminhao_azul.cor, caminhao_azul.rodas, caminhao_azul.marca)