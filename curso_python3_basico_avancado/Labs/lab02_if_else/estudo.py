# Estruturas Condicionais em Python

# As estruturas condicionais são fundamentais em qualquer linguagem de programação, pois permitem tomar
# decisões com base em condições lógicas. Em Python, trabalhamos principalmente com:

# if
# elif
# else

# Este guia traz explicações claras, exemplos, boas práticas e pegadinhas comuns.

# 1. O que é uma condição?
# Uma condição é uma expressão que avalia para Verdadeiro (True) ou Falso (False).
# Em Python, além de True e False, outros valores também são considerados verdadeiros ou falsos.

# Valores Falsy (tratados como False):
# False
# 0 (de qualquer tipo numérico)
# None
# "" (string vazia)
# [] (lista vazia)
# {} (dicionário vazio)
# set() (conjunto vazio)

# Valores Truthy (tratados como True):
# Quase tudo que não estiver na lista acima.

# 2. Estrutura básica do if

# if condição:
    # bloco executado se condição for verdadeira

# Exemplo:

# idade = 20
# if idade >= 18:
#     print("Maior de idade")

# 3. Estrutura completa: if, elif, else

x = 10

if x > 10:
    print("Maior que 10")
elif x == 10:
    print("Igual a 10")
else:
    print("Menor que 10")

# Regras importantes
# Pode haver vários elif
# Só pode existir um else, ao final
# A indentação é obrigatória (4 espaços é o padrão)


# --------------------------------------------------
# Código melhorado e exemplos para estudo prático
# --------------------------------------------------

def truthy_falsy_demo() -> None:
    """Imprime exemplos de valores truthy e falsy.

    Útil para entender como expressões são avaliadas em condições.
    """
    examples = {
        "Falsy": [False, 0, 0.0, None, "", [], {}, set()],
        "Truthy": [True, 1, -1, "texto", [1], {"a": 1}, (0,)]
    }
    for k, vals in examples.items():
        print(f"{k}:")
        for v in vals:
            print(f"  {repr(v)} -> {bool(v)}")


def classify_number(n: int) -> str:
    """Classifica um número como 'positive', 'zero' ou 'negative'.

    Exemplos:
    >>> classify_number(5)
    'positive'
    >>> classify_number(0)
    'zero'
    >>> classify_number(-3)
    'negative'
    """
    if n > 0:
        return "positive"
    elif n == 0:
        return "zero"
    else:
        return "negative"


def grade_letter(score: float) -> str:
    """Converte uma nota (0-100) em conceito A-F usando if/elif/else.

    Levanta ValueError se a nota estiver fora do intervalo.

    >>> grade_letter(95)
    'A'
    >>> grade_letter(73)
    'C'
    >>> grade_letter(10)
    'F'
    """
    if not (0 <= score <= 100):
        raise ValueError("Score precisa estar entre 0 e 100")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def is_leap_year(year: int) -> bool:
    """Retorna True se o ano for bissexto.

    Regras:
    - Divisível por 4
    - Exceto se divisível por 100, a menos que divisível por 400

    >>> is_leap_year(2000)
    True
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2024)
    True
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def ternary_example(n: int) -> str:
    """Exemplo de operador ternário para verificar par/ímpar."""
    return "even" if n % 2 == 0 else "odd"


def main() -> None:
    print("--- Truthy / Falsy demo ---")
    truthy_falsy_demo()
    print("\n--- Classify Number ---")
    for n in (10, 0, -5):
        print(n, "->", classify_number(n))
    print("\n--- Grade Letters ---")
    for s in (95, 82, 76, 61, 50):
        print(s, "->", grade_letter(s))
    print("\n--- Leap Year Examples ---")
    for y in (1999, 2000, 1900, 2024):
        print(y, "bissexto?", is_leap_year(y))
    print("\n--- Ternary Example ---")
    for n in (2, 3):
        print(n, "->", ternary_example(n))


if __name__ == "__main__":
    main()

