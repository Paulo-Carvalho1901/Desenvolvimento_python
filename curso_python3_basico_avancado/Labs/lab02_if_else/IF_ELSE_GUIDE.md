# Guia Completo: Estruturas Condicionais (if / elif / else) ✅

Este documento apresenta explicações concisas, exemplos reais e exercícios com solução para dominar estruturas condicionais em Python.

## 1. Objetivo 🎯
- Entender como avaliar condições (truthy/falsy)
- Usar `if`, `elif`, `else` de forma clara e legível
- Conhecer operadores de comparação, lógicos, e armadilhas comuns
- Praticar com exercícios aplicáveis ao curso

## 2. Conceitos fundamentais 💡
- Uma condição é avaliada como `True` ou `False`.
- Valores 'falsy': `False`, `0`, `None`, `""`, `[]`, `{}`, `set()`.
- Tudo que não for falsy é considerado `True` (truthy).

## 3. Sintaxe básica
```python
if condicao:
    # executa quando condicao é True
elif outra_condicao:
    # executa se a primeira for False e esta for True
else:
    # executa se todas anteriores forem False
```

## 4. Operadores úteis
- Comparação: `==`, `!=`, `<`, `<=`, `>`, `>=`
- Lógicos: `and`, `or`, `not` (curto-circuito: `and` para falsidade, `or` para verdade)
- Encadeamento: `0 < x < 10` (equivalente a `0 < x and x < 10`)
- Ternário: `a if cond else b` (expressão, não declaração)

## 5. Boas práticas e armadilhas ⚠️
- Use `is` apenas para comparar identidade (ex.: `x is None`), e `==` para igualdade de valor.
- Evite lógica pesada em uma única linha — prefira clareza.
- Lembre-se de validar entradas (ex.: notas entre 0 e 100).

## 6. Exemplos práticos (veja `estudo.py`)
- `truthy_falsy_demo()` — demonstra `bool()` em valores comuns
- `classify_number(n)` — exemplo simples com `if/elif/else`
- `grade_letter(score)` — uso de intervalos e validação
- `is_leap_year(year)` — regra com `elif` encadeado
- `ternary_example(n)` — operador condicional compacto

## 7. Exercícios ✍️
1. Escreva uma função `fizzbuzz(n)` que retorna `"Fizz"` se n divisível por 3, `"Buzz"` se divisível por 5, `"FizzBuzz"` se por ambos, ou `str(n)` caso contrário. Teste com os números 1..20.
2. Reescreva `grade_letter` usando menos branches (pistas: tabelas, `bisect` ou listas ordenadas).
3. Escreva `classify_temperature(t)` que retorna `'freezing'` se t <= 0, `'cold'` se 1-15, `'warm'` 16-25, `'hot'` >25.

### Soluções rápidas
- `fizzbuzz`: veja `Labs/lab02_if_else/solutions_fizzbuzz.py` (se criado) ou implemente com `if x % 15 == 0` primeiro.
- `grade_letter (alternativa)`: usar thresholds = [90,80,70,60] e percorrer.

## 8. Como usar
- Executar exemplos: `python3 Labs/lab02_if_else/estudo.py`
- Rodar testes (se existir): `pytest -q`

---
