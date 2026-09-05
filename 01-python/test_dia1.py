import json

import pytest

from dia1_funcoes import (
    carregar_json_seguro,
    contar_palavras,
    dividir_com_seguranca,
    media,
    pares_ao_quadrado,
)


def test_media():
    assert media([1, 2, 3]) == 2
    assert media([10]) == 10


def test_pares_ao_quadrado():
    assert pares_ao_quadrado([1, 2, 3, 4, 5]) == [4, 16]
    assert pares_ao_quadrado([1, 3, 5]) == []


def test_contar_palavras():
    assert contar_palavras("oi oi tudo bem") == {"oi": 2, "tudo": 1, "bem": 1}


def test_dividir_com_seguranca_normal():
    assert dividir_com_seguranca(10, 2) == 5


def test_dividir_com_seguranca_por_zero():
    assert dividir_com_seguranca(10, 0) is None


def test_carregar_json_seguro_arquivo_valido(tmp_path):
    arquivo = tmp_path / "dados.json"
    arquivo.write_text(json.dumps({"a": 1}), encoding="utf-8")
    assert carregar_json_seguro(str(arquivo)) == {"a": 1}


def test_carregar_json_seguro_arquivo_inexistente():
    assert carregar_json_seguro("nao_existe.json") == {}


def test_carregar_json_seguro_json_invalido(tmp_path):
    arquivo = tmp_path / "invalido.json"
    arquivo.write_text("{isso nao e json valido", encoding="utf-8")
    assert carregar_json_seguro(str(arquivo)) == {}
