#UMA API É UM JEITO DE CONECTAR SISTEMAS, INTERFACE DE PROGRAÇÃO DE APLICAÇÕES;
#API É UM CONJUNTO DE REGRAS E PADRÕES QUE PERMITE QUE DIFERENTES SISTEMAS
#DE SOFTWARE SE COMUNIQUEM E TROQUEM DADOS ENTRE SÍ;

#NESTE EXEMPLO SERÁ UTILIZADO A WEATHERapi.com PARA CONSULTAR AS CONDIÇÕES
#CLIMÁTICAS DE UMA DETERMINADA LOCALIDADE;

#CONTRUIR API -> 32762b1f452f44e186b224534262909
#VAMOS PRECISAR DE UM PROGRAMA QUE TENHA UMA CERTA CAPACIDADE DE PEGAR DADOS
#MEDIANTE A UMA URL PRÉ DEFINIDA

import requests #biblioteca para fazer requisições HTTP
from pprint import pprint #biblioteca para imprimir os dados de forma legível

#VAMOS PRECISAR DE APIKEY -> UMA CREDENCIAL
API_Key = "32762b1f452f44e186b224534262909"
API_Link = "http://api.weatherapi.com/v1/current.json"

cidade = str(input("Qual cidade deseja? "))
linguagem =  str(input("Qual linguagem deseja? "))

parametros = {
"key":API_Key,
"q":cidade,#cidade para qual queremos obter os dados
"lang":linguagem,#linguagem
"humidity":"" #Umidade
}

#armazenando a resposta da requisição na variavel resposta
resposta = requests.get(API_Link,params = parametros)

print(resposta.status_code)
#status code: 200(sucesso) ou 401(erro)/404(não encontrado)
#print(resposta.content)

if resposta.status_code == 200:
    print("Requisição realizada com sucesso!")
    dados = resposta.json()#armazenando os dados em formato json na variável dados
    #pprint(dados)
    temperatura = dados["current"]["temp_c"]#armazenando a temp em °C
    descricao = dados["current"]["condition"]["text"]#armazenando a descrição
    umidade = dados["current"]["humidity"]
    print(f"A temperatura atual é de {temperatura}°C")
    print(f"Descrição do clima: {descricao}")
    print(f"O local está com {umidade}% de humidade")
else:
    print("Erro na requisição.")
