"""
Dia 1 - Semana 1: funções, comprehensions e try/except.

Implemente as funções abaixo. Rode os testes com:
    venv\\Scripts\\python.exe -m pytest 01-python/test_dia1.py -v

"""
import json


def media(numeros: list[float]) -> float:
    media_lista = sum(numeros) / len(numeros)

    return media_lista


def pares_ao_quadrado(numeros: list[int]) -> list[int]:
    """Retorna o quadrado de cada número PAR da lista, usando list comprehension."""
    return [numeros ** 2 for numeros in numeros if numeros % 2 == 0]


def contar_palavras(texto: str) -> dict[str, int]:
    """Retorna um dicionário {palavra: quantidade de vezes que aparece} no texto.

    Ex: contar_palavras("oi oi tudo bem") -> {"oi": 2, "tudo": 1, "bem": 1}
    Use dict comprehension ou um loop simples, como preferir.
    """

    palavras = texto.split()
    return {palavra: palavras.count(palavra) for palavra in set(palavras)}


def dividir_com_seguranca(a: float, b: float) -> float | None:
    """Divide a por b. Se b for zero, retorna None em vez de lançar exceção.

        Use try/except para capturar ZeroDivisionError.
        """

    try:
        return a/b

    except ZeroDivisionError:

        return None



def carregar_json_seguro(caminho: str) -> dict:
    """Lê um arquivo JSON no caminho informado e retorna o dicionário.

    Se o arquivo não existir ou o conteúdo for JSON inválido, retorna {} (dicionário vazio)
    em vez de deixar a exceção propagar.
    """

    try:
      with open(caminho) as arquivo:
          return json.load(arquivo)


    except (FileNotFoundError, json.JSONDecodeError):
        return {}
