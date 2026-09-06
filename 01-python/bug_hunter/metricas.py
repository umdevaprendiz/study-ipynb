"""
Projeto 1 - Bug Hunter.

Este módulo simula métricas de benchmark de um sistema de IA (latência, taxa de
acerto, custo, filtragem de respostas). Ele tem bugs intencionais.

Rode os testes com:
    venv\\Scripts\\python.exe -m pytest 01-python/bug_hunter/test_metricas.py -v

Leia a saída de cada falha, entenda o que a função deveria fazer (docstring +
teste), ache o bug no código abaixo e corrija um de cada vez. Rode os testes
de novo depois de cada correção.
"""


def media_latencia(latencias: list[float]) -> float:
    """Retorna a latência média (em segundos) de uma lista de chamadas."""
    return sum(latencias) / len(latencias)


def taxa_acerto(respostas_corretas: int, total: int) -> float:
    """Retorna a taxa de acerto em porcentagem (0 a 100)."""
    return (respostas_corretas / total) * 100


def filtrar_respostas_validas(respostas: list[str]) -> list[str]:
    """Remove respostas vazias ('') ou None da lista, mantendo só as válidas."""
    return [x for x in respostas if x is not None and x != ""]


def custo_total(tokens_por_chamada: list[int], preco_por_token: float) -> float:
    """Calcula o custo total, dado o número de tokens usados em cada chamada
    e o preço por token."""
    return len(tokens_por_chamada) * preco_por_token


def resumo_benchmark(latencias: list[float], respostas_corretas: int, total: int) -> dict:
    """Monta um resumo com latência média e taxa de acerto do benchmark."""
    return {
        "latencia_media": media_latencia(latencias),
        "taxa_acerto": taxa_acerto(respostas_corretas, total),
    }
