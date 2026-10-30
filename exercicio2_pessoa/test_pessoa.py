import pytest

from exercicio2_pessoa.pessoa import (
    EMAIL_INVALIDO,
    EMAIL_OBRIGATORIO,
    IDADE_INTERVALO,
    NOME_LETRAS,
    NOME_PARTES,
    Email,
    Person,
    PersonDAO,
)

dao = PersonDAO()
proximo_id = iter(range(1, 10_000))


def email(nome):
    return Email(next(proximo_id), nome)


def person(nome, idade, emails=None):
    return Person(next(proximo_id), nome, idade, emails)


def test_pessoa_valida_nao_retorna_erros():
    p = person("Joao Silva", 30, [email("joao.silva@email.com")])
    assert dao.isValidToInclude(p) == []


def test_save_armazena_pessoa():
    p = person("Joao Silva", 30, [email("joao.silva@email.com")])
    dao_local = PersonDAO()
    dao_local.save(p)
    assert p in dao_local._pessoas


@pytest.mark.parametrize("nome", ["Joao", "", "   "])
def test_nome_com_menos_de_duas_partes(nome):
    erros = dao.isValidToInclude(person(nome, 30, [email("a@b.com")]))
    assert NOME_PARTES in erros


@pytest.mark.parametrize("nome", ["Jo4o Silva", "Joao Silv@", "Joao _Silva"])
def test_nome_com_caracteres_que_nao_sao_letras(nome):
    erros = dao.isValidToInclude(person(nome, 30, [email("a@b.com")]))
    assert NOME_LETRAS in erros


@pytest.mark.parametrize("idade", [0, -1, 201, 1000])
def test_idade_fora_do_intervalo(idade):
    erros = dao.isValidToInclude(person("Joao Silva", idade, [email("a@b.com")]))
    assert IDADE_INTERVALO in erros


@pytest.mark.parametrize("idade", [1, 200])
def test_idade_nos_limites_do_intervalo(idade):
    erros = dao.isValidToInclude(person("Joao Silva", idade, [email("a@b.com")]))
    assert IDADE_INTERVALO not in erros


def test_pessoa_sem_email():
    erros = dao.isValidToInclude(person("Joao Silva", 30))
    assert EMAIL_OBRIGATORIO in erros


def test_pessoa_com_lista_de_emails_vazia():
    erros = dao.isValidToInclude(person("Joao Silva", 30, []))
    assert EMAIL_OBRIGATORIO in erros


@pytest.mark.parametrize(
    "endereco",
    ["sem-arroba.com", "@email.com", "joao@email", "joao@.com", "joao@email.", "joao @email.com"],
)
def test_email_fora_do_formato(endereco):
    erros = dao.isValidToInclude(person("Joao Silva", 30, [email(endereco)]))
    assert EMAIL_INVALIDO.format(nome=endereco) in erros


@pytest.mark.parametrize("endereco", ["a@b.c", "joao.silva@email.com", "joao+tag@email.com.br"])
def test_emails_validos(endereco):
    erros = dao.isValidToInclude(person("Joao Silva", 30, [email(endereco)]))
    assert not any(e.startswith("Email invalido") for e in erros)


def test_erros_acumulados_sao_retornados():
    p = person("Joao", 0, [email("invalido")])
    erros = dao.isValidToInclude(p)
    assert NOME_PARTES in erros
    assert IDADE_INTERVALO in erros
    assert EMAIL_INVALIDO.format(nome="invalido") in erros
