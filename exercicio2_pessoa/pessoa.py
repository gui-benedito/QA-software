import re

NOME_PARTES = "O nome deve ter ao menos 2 partes"
NOME_LETRAS = "O nome deve conter apenas letras"
IDADE_INTERVALO = "A idade deve estar entre 1 e 200"
EMAIL_OBRIGATORIO = "A pessoa deve ter ao menos um email"
EMAIL_INVALIDO = "Email invalido: {nome}"


class Email:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome


class Person:
    def __init__(self, id: int, nome: str, idade: int, emails: list[Email] | None = None):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.emails = emails if emails is not None else []


class PersonDAO:
    _EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def __init__(self):
        self._pessoas: list[Person] = []

    def save(self, p: Person) -> None:
        self._pessoas.append(p)

    def isValidToInclude(self, p: Person) -> list[str]:
        erros = []

        partes = p.nome.split()
        if len(partes) < 2:
            erros.append(NOME_PARTES)
        if not all(parte.isalpha() for parte in partes):
            erros.append(NOME_LETRAS)

        if not 1 <= p.idade <= 200:
            erros.append(IDADE_INTERVALO)

        if len(p.emails) == 0:
            erros.append(EMAIL_OBRIGATORIO)

        for email in p.emails:
            if not self._EMAIL_REGEX.match(email.nome):
                erros.append(EMAIL_INVALIDO.format(nome=email.nome))

        return erros
