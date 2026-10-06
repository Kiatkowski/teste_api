import requests

BASE_URL = "https://economia.awesomeapi.com.br/json/last"

MOEDAS = {
    "USD-BRL": "Dólar Americano",
    "EUR-BRL": "Euro",
    "GBP-BRL": "Libra Esterlina",
    "ARS-BRL": "Peso Argentino",
    "BTC-BRL": "Bitcoin",
    "ETH-BRL": "Ethereum",
}


def get_cotacao(par: str) -> dict:
    """Consulta a cotação de um par (ex.: 'USD-BRL') e retorna os dados dele."""
    response = requests.get(f"{BASE_URL}/{par}", timeout=10)

    if response.status_code == 404:
        info = response.json()
        raise RuntimeError(info.get("message", "Moeda não encontrada."))

    if response.status_code != 200:
        raise RuntimeError(
            f"Erro ao consultar a API. Status: {response.status_code}"
        )

    # A API devolve {"USDBRL": {...}}, ou seja, a chave é o par sem o hífen
    return response.json()[par.replace("-", "")]