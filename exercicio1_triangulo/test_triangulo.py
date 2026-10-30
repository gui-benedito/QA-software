from itertools import permutations

import pytest

from exercicio1_triangulo.triangulo import classificar_triangulo


def test_triangulo_escaleno_valido():
    assert classificar_triangulo(3, 4, 5) == "escaleno"


def test_triangulo_equilatero_valido():
    assert classificar_triangulo(5, 5, 5) == "equilatero"


@pytest.mark.parametrize("a,b,c", [(5, 5, 3), (5, 3, 5), (3, 5, 5)])
def test_triangulo_isosceles_valido_permutacoes(a, b, c):
    assert classificar_triangulo(a, b, c) == "isosceles"


def test_um_valor_zero():
    assert classificar_triangulo(0, 4, 5) == "nao e um triangulo"


def test_um_valor_negativo():
    assert classificar_triangulo(-1, 4, 5) == "nao e um triangulo"


@pytest.mark.parametrize("a,b,c", list(permutations([1, 2, 3])))
def test_soma_de_dois_lados_igual_ao_terceiro(a, b, c):
    assert classificar_triangulo(a, b, c) == "nao e um triangulo"


@pytest.mark.parametrize("a,b,c", list(permutations([1, 2, 4])))
def test_soma_de_dois_lados_menor_que_o_terceiro(a, b, c):
    assert classificar_triangulo(a, b, c) == "nao e um triangulo"


def test_tres_valores_iguais_a_zero():
    assert classificar_triangulo(0, 0, 0) == "nao e um triangulo"
