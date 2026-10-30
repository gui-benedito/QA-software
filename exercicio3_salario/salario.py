from decimal import ROUND_HALF_UP, Decimal
from enum import Enum


class Cargo(Enum):
    DESENVOLVEDOR = "DESENVOLVEDOR"
    DBA = "DBA"
    TESTADOR = "TESTADOR"
    GERENTE = "GERENTE"


class Funcionario:
    def __init__(self, nome: str, email: str, salario_base: Decimal, cargo: Cargo):
        self.nome = nome
        self.email = email
        self.salario_base = salario_base
        self.cargo = cargo


class CalculadoraSalario:
    _DESCONTOS = {
        Cargo.DESENVOLVEDOR: (Decimal("3000"), Decimal("0.20"), Decimal("0.10")),
        Cargo.DBA: (Decimal("2000"), Decimal("0.25"), Decimal("0.15")),
        Cargo.TESTADOR: (Decimal("2000"), Decimal("0.25"), Decimal("0.15")),
        Cargo.GERENTE: (Decimal("5000"), Decimal("0.30"), Decimal("0.20")),
    }

    def calcular_salario_liquido(self, funcionario: Funcionario) -> Decimal:
        limite, desconto_alto, desconto_baixo = self._DESCONTOS[funcionario.cargo]
        desconto = desconto_alto if funcionario.salario_base >= limite else desconto_baixo
        liquido = funcionario.salario_base * (Decimal("1") - desconto)
        return liquido.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
