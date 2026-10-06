import requests

menu_moedas = """

=== Opções de Moedas para Consulta ===

Tradicionais:

USD-BRL (Dólar Americano)
EUR-BRL (Euro)
GBP-BRL (Libra Esterlina)
ARS-BRL (Peso Argentino)

Criptomoedas:

BTC-BRL (Bitcoin)
ETH-BRL (Ethereum)
======================================

"""
print(menu_moedas)

def consultar_moeda(moeda): 
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        print("Deu certo!")
        print(resposta.json())
        return resposta.json()
    
    elif resposta.status_code == 404:
        numero = resposta.json()
        status = numero.get("status")
        print(f"Status com erro: {status}")
        code = numero.get("code")
        print(f"Codigo do erro: {code}")
        message = numero.get("message")
        print(f"Mensagem do erro: {message}")

    else: print("deu ruim!")

moeda_desejada = input("Digite qual moeda deseja consultar (ex:USD-BRL): ")

dados_api = consultar_moeda(moeda_desejada)

if dados_api:
    chave = moeda_desejada.replace("-","")
    valor = dados_api[chave]["bid"]
    print("\nRequisição bem-sucedida!")

    print(f"O valor atual de {moeda_desejada} é: ")
    print(f"R$ {float(valor):.2f}")

else:
    print(f"\nErro ao consultar a moeda: {moeda_desejada} \nVerifique se o formato está correto")