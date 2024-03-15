import requests

try:
    requi = requests.get('https://solyd.com.br')
    print(requi.text)
except requests.exceptions.RequestException as e:
    print("Erro ao fazer a requisição:", e)