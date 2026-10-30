# QA-software

Repositório da atividade de **Teste de Software** com implementação dos três exercícios em **Python**, usando **pytest** para os testes e **pytest-cov** para as evidências de cobertura.

## Stack

- Python 3.13
- pytest 8
- pytest-cov

## Estrutura do projeto

```
.
├── exercicio1_triangulo/
│   ├── triangulo.py            # classificação de triângulos
│   └── test_triangulo.py       # casos de teste
├── exercicio2_pessoa/
│   ├── pessoa.py               # Person, Email e PersonDAO (TDD)
│   └── test_pessoa.py          # casos de teste
├── exercicio3_salario/
│   ├── salario.py              # calculadora de salário líquido (TDD)
│   └── test_salario.py         # casos de teste
├── .coveragerc                 # configuração de cobertura (inclui branches)
├── pytest.ini                  # configuração do pytest
└── requirements.txt
```

## Pré-requisitos

- Python 3.10 ou superior (o projeto foi validado no Python 3.13.3)
- pip

## Build (preparação do ambiente)

```bash
python -m venv .venv
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Linux/macOS
source .venv/bin/activate

python -m pip install -r requirements.txt
```

## Execução dos testes

Todos os exercícios:

```bash
python -m pytest
```

Por exercício:

```bash
python -m pytest exercicio1_triangulo
python -m pytest exercicio2_pessoa
python -m pytest exercicio3_salario
```

## Evidências de cobertura de código

A cobertura é medida com `pytest-cov`, incluindo cobertura de **branches** (configurada em `.coveragerc`). Os arquivos de teste são omitidos do relatório para mostrar apenas o código de produção.

### Exercício 1 - Triângulo

```bash
python -m pytest exercicio1_triangulo --cov=exercicio1_triangulo --cov-report=term-missing
```

```text
....................                                                     [100%]

---------- coverage: platform win32, python 3.13.3-final-0 -----------
Name                                Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------------------
exercicio1_triangulo\__init__.py        0      0      0      0   100%
exercicio1_triangulo\triangulo.py      10      0      8      0   100%
-------------------------------------------------------------------------------
TOTAL                                  10      0      8      0   100%

20 passed in 0.08s
```

Casos de teste cobertos: escaleno válido, isósceles válido (3 permutações de 5,5,3), equilátero válido, valor zero, valor negativo, soma de dois lados igual ao terceiro (6 permutações de 1,2,3), soma de dois lados menor que o terceiro (6 permutações de 1,2,4) e os três lados iguais a zero.

### Exercício 2 - Pessoa e Email (TDD)

```bash
python -m pytest exercicio2_pessoa --cov=exercicio2_pessoa --cov-report=term-missing
```

```text
..........................                                               [100%]

---------- coverage: platform win32, python 3.13.3-final-0 -----------
Name                            Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------
exercicio2_pessoa\__init__.py       0      0      0      0   100%
exercicio2_pessoa\pessoa.py        37      0     12      0   100%
---------------------------------------------------------------------------
TOTAL                              37      0     12      0   100%

26 passed in 0.13s
```

Classes modeladas conforme o diagrama: `Person` (`id`, `nome`, `idade`, `emails`), `Email` (`id`, `nome`) e `PersonDAO` (`save(p)` e `isValidToInclude(p)`).

Casos de teste cobertos: pessoa válida, `save` armazenando a pessoa, nome com menos de duas partes, nome com caracteres não alfabéticos, idade nos limites e fora do intervalo [1, 200], pessoa sem e-mail, e-mails fora do formato e e-mails válidos, além de acúmulo de múltiplos erros.

### Exercício 3 - Calculadora de salário (TDD)

```bash
python -m pytest exercicio3_salario --cov=exercicio3_salario --cov-report=term-missing
```

```text
.............                                                            [100%]

---------- coverage: platform win32, python 3.13.3-final-0 -----------
Name                             Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------
exercicio3_salario\__init__.py       0      0      0      0   100%
exercicio3_salario\salario.py       20      0      0      0   100%
----------------------------------------------------------------------------
TOTAL                               20      0      0      0   100%

13 passed in 0.07s
```

Casos de teste cobertos: cada cargo (DESENVOLVEDOR, DBA, TESTADOR e GERENTE) nos valores de salário abaixo, no limite e acima do limite de desconto, além do arredondamento para duas casas decimais.

## Resultado geral

```bash
python -m pytest
```

```text
...........................................................              [100%]
59 passed
```

## Sobre o TDD (Exercícios 2 e 3)

Os exercícios 2 e 3 foram desenvolvidos seguindo o ciclo **Red-Green-Refactor** do TDD: os testes foram escritos antes da implementação, partindo de casos que falhavam e evoluindo até a implementação mínima que os fazia passar, seguida de refatoração do código.
