import pytest

from metricas import (
    custo_total,
    filtrar_respostas_validas,
    media_latencia,
    resumo_benchmark,
    taxa_acerto,
)


def test_media_latencia():
    assert media_latencia([1.0, 2.0, 4.0]) == pytest.approx(2.3333, rel=1e-3)


def test_taxa_acerto():
    assert taxa_acerto(8, 10) == 80


def test_filtrar_respostas_validas():
    assert filtrar_respostas_validas(["oi", None, "", "tudo bem"]) == ["oi", "tudo bem"]


def test_custo_total():
    assert custo_total([100, 200, 50], 0.01) == pytest.approx(3.5)


def test_resumo_benchmark():
    resumo = resumo_benchmark([1.0, 2.0, 4.0], 8, 10)
    assert resumo["latencia_media"] == pytest.approx(2.3333, rel=1e-3)
    assert resumo["taxa_acerto"] == 80
