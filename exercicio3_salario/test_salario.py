from decimal import Decimal

import pytest

from exercicio3_salario.salario import CalculadoraSalario, Cargo, Funcionario

calculadora = CalculadoraSalario()


def funcionario(cargo, salario):
    return Funcionario("Ana", "ana@email.com", Decimal(salario), cargo)


@pytest.mark.parametrize(
    "cargo,salario,esperado",
    [
        (Cargo.DESENVOLVEDOR, "3000", "2400.00"),
        (Cargo.DESENVOLVEDOR, "2999.99", "2699.99"),
        (Cargo.DESENVOLVEDOR, "1000", "900.00"),
        (Cargo.DBA, "2000", "1500.00"),
        (Cargo.DBA, "1999.99", "1699.99"),
        (Cargo.DBA, "1000", "850.00"),
        (Cargo.TESTADOR, "2000", "1500.00"),
        (Cargo.TESTADOR, "1999.99", "1699.99"),
        (Cargo.TESTADOR, "1000", "850.00"),
        (Cargo.GERENTE, "5000", "3500.00"),
        (Cargo.GERENTE, "4999.99", "3999.99"),
        (Cargo.GERENTE, "1000", "800.00"),
    ],
)
def test_calculo_do_salario_liquido(cargo, salario, esperado):
    assert calculadora.calcular_salario_liquido(funcionario(cargo, salario)) == Decimal(esperado)


def test_arredondamento_para_duas_casas():
    resultado = calculadora.calcular_salario_liquido(funcionario(Cargo.DESENVOLVEDOR, "3333.33"))
    assert resultado == Decimal("2666.66")
