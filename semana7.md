# PI - Semana 7

## Conjuntos

Até agora usamos listas (dados do tipo `list`) para armazenar coleções de dados. Vimos que uma lista em Python permite a inclusão de valores de diferentes tipos, incluindo valores repetidos. Além disso, também permite que os valores possam ser acessados e modificados via indexação. Por exemplo, `x[0]` acessa o primeiro elemento da lista `x`.

Uma outra coleção de dados fornecida pela linguagem Python é o **conjunto**, de tipo de dado `set`. Diferente da lista, um conjunto não permite elementos duplicados. Além disso, não permite indexação e não permite que um elemento seja modificado. Entretanto, podemos remover um elemento e inserir um novo.

Para criar um conjunto usamos chaves e colocamos os elementos do conjunto separados por vírgula:

```python
# Criando um conjunto
cjt = {"UFABC", True, 42, 3.1415}
```

O tipo de dado de um conjunto é `set`. Veja no REPL:

```
>>> type(cjt)
<class 'set'>
```

Valores duplicados são ignorados quando um conjunto é criado:

```
>>> cjt = {"UFABC", True, "UFABC", 42, 3.1415}
>>> cjt
{True, 42, 3.1415, 'UFABC'}
```

Os valores `True` e `1` são considerados como valores duplicados em um conjunto:

```
>>> x = {True, 1}
>>> x
{True}
>>> x = {1, True}
>>> x
{1}
```

Um número inteiro (por exemplo, `2`) e seu correspondente em ponto flutuante (por exemplo, `2.0`) também são considerados como valores duplicados em um conjunto:

```
>>> {2, 2.0}
{2}
```


## Operadores `in` e `not in`

Podemos verificar se um dado elemento existe em um conjunto através do operador `in`:

```
>>> cjt = {"UFABC", True, 42, 3.1415}
>>> "UFABC" in cjt
True
```

O resultado é `True` pois `"UFABC"` é um elemento do conjunto `cjt`.

Também podemos usar o operador `not in` para verificar se um dado valor não existe no conjunto:

```
>>> 34 not in cjt
True
```

O resultado é `True` pois 34 não faz parte de `cjt`.

Os operadores `in` e `not in` também podem ser usados com **listas** e **strings**:

```
>>> 10 in [2, -5, 10, 3, 83]
True
>>> 4 not in [2, -5, 10, 3, 83]
True
>>> "U" in "UFABC"
True
```

## Tamanho do conjunto

O tamanho de um conjunto é o seu número de elementos. O tamanho é obtido com a função embutida `len()`:

```
>>> x = {20, 5.2, False, "UFABC"}
>>> len(x)
4
```

## Diferentes formas de criar um conjunto

Podemos criar um **conjunto vazio** com `set()`:

```
>>> vazio = set()
>>> len(vazio)
0
```

> **Observação:** não use `{}` para criar um conjunto vazio. O resultado será um dado do tipo `dict` (dicionário), que é outro tipo de coleção de dados do Python.

Também podemos criar um conjunto não vazio com `set()` passando como argumento uma tupla, isto é, valores separados por vírgula dentro de parênteses:

```
>>> set((42, True, "Olá"))
{True, 42, 'Olá'}
```

A função `set()` também pode ser usada para converter uma string em um conjunto:

```
>>> set("UFABC")
{'F', 'A', 'B', 'U', 'C'}
```

Observe que a ordem dos elementos do conjunto não é necessariamente a ordem dos caracteres na string. **Um conjunto é uma coleção não ordenada de dados.**

Um conjunto pode ser criado a partir de uma lista, e vice-versa:

```
>>> x = [42, True, 42, "Olá"]
>>> y = set(x)
>>> y
{True, 42, "Olá"}
>>> z = list(y)
>>> z
[True, 42, 'Olá']
```

## Adicionando um elemento a um conjunto

Para adicionar um elemento a um conjunto podemos usar o método `add(elem)`, onde `elem` é o elemento que queremos adicionar:

```
>>> x = {5, 10, 2}
>>> x.add(3)
>>> x
{3, 10, 2, 5}
```

## Removendo um elemento de um conjunto

O método `remove(elem)` remove o elemento `elem` do conjunto:

```
>>> x = {5, 10, 2, 3}
>>> x.remove(10)
>>> x
{2, 3, 5}
```


## Copiando conjuntos

As mesmas considerações que vimos sobre cópia de listas se aplica à cópia de conjuntos. Para copiar (clonar) um conjunto, devemos usar o método `copy()` ou a função `set()`:

```
>>> a = {5, 10, 2, 3}
>>> b = a.copy()
>>> c = set(a)
>>> a is b
False
>>> a is c
False
```

## Iterando sobre um conjunto

Uma vez que não podemos usar indexação para acessar os elementos de um conjunto, só é possível iterar sobre um conjunto através da sintaxe `for elemento in conjunto`:

```python
x = {5, 10, 2, 3}
for elem in x:
    print(elem)
```


## Outros métodos de `set`

Supondo que `x` e `y` são conjuntos:

Método        | Descrição
:-----        | :-----    
`x.clear()`     | Remove todos os elementos de `x`.
`x.difference(y)`| Retorna a diferença entre os conjuntos (elementos que existem só em `x`).
`x.intersection(y)`| Retorna a interseção dos conjuntos.
`x.symmetric_difference(y)` | Retorna a diferença simétrica entre os conjuntos (elementos de `x` e `y`, exceto os elementos presentes nos dois conjuntos).
`x.union(y)`  | Retorna a união dos conjuntos.
`x.update(y)` | Insere os elementos de `y` em `x`.
`x.issubset(y)` | Retorna `True` se todos os itens de `x` estão presentes em `y`.
`x.issuperset(y)` | Retorna `True` se todos os itens de `y` estão presents em `x`.
`x.pop()` | Remove um elemento aleatório de `x` e retorna-o.

> **Exercício 7.1 - Existência de duplicados (1)**
>
> Faça uma função `tem_duplicados1(x)` que recebe uma lista `x` e retorna `True` caso existam elementos duplicados em `x`. Faça a função sem usar conjuntos (sem usar o tipo de dado `set`). Use apenas listas.
>
> Exemplos:
> * `tem_duplicados1([10, 2, -3, 7, 11, 10])` deverá retornar `True`.
> * `tem_duplicados1(["UFABC", 2, True, 3.0, "ufabc"])` deverá retornar `False`.
> * `tem_duplicados1([10, 2, -3, 7, 11, 3])` deverá retornar `False`.
> * `tem_duplicados1([True, 1])` deverá retornar `True`.
> * `tem_duplicados1([3, 3.0])` deverá retornar `True`.
> ***

> **Exercício 7.2 - Existência de duplicados (2)**
>
> Faça uma função `tem_duplicados2(x)` que recebe uma lista `x` e retorna `True` caso existam elementos duplicados em `x`. Use o tipo de dado `set` para simplificar a função.
>
> ***

> **Exercício 7.3 - Contar duplicados**
>
> Faça uma função `contar_duplicados(x)` que recebe uma lista `x` e retorna quantos elementos de `x` ocorrem mais do que uma vez.
>
> Exemplos:
> * `contar_duplicados([10])` deverá retornar `0`.
> * `contar_duplicados([10, 10, 10, 10])` deverá retornar `1`.
> * `contar_duplicados([10, 2, 2, 7, 10, 10])` deverá retornar `2`.
> * `contar_duplicados(["UFABC", 2, True, 3.0, "ufabc"])` deverá retornar `0`.
>
> ***

> **Exercício 7.4 - Enumerar duplicados**
>
> Faça uma função `enumerar_duplicados(x)` que recebe uma lista `x` e retorna o conjunto dos elementos duplicados em `x`.
>
> Exemplos:
> * `enumerar_duplicados([10])` deverá retornar um conjunto vazio (`set()`).
> * `enumerar_duplicados([10, 10, 10, 10])` deverá retornar `{10}`.
> * `enumerar_duplicados([10, 2, 2, 7, 10, 10])` deverá retornar `{10, 2}`.
> * `enumerar_duplicados(["UFABC", 2, True, 3.0, "ufabc"])` deverá retornar um conjunto vazio (`set()`).
>
> ***

> **Exercício 7.5 - Sorteio**
>
> Faça uma função `sorteio(apostas)`, onde `apostas` é um conjunto de inteiros no intervalo `[0, 999]`. A função deve gerar números aleatórios no intervalo `[0, 999]` até que todos os números em `apostas` tenham sido obtidos ao menos uma vez. Retorne a quantidade de sorteios (números aleatórios gerados) necessários para atingir esse objetivo.
>
> * Calcule o valor médio de `sorteio({0})` considerando 10 mil execuções. O resultado deve ser em torno de 1000.
> * Calcule o valor médio de `sorteio({0, 1})` considerando 10 mil execuções. O resultado deve ser em torno de 1500.
>
> ***

> **Exercício 7.6 - Jogo da Forca**
>
> Faça um "Jogo da Forca". O jogador deve adivinhar as letras da palavra oculta e não pode errar mais que 5 vezes. A cada jogada, mostre quais letras da palavra oculta já foram descobertas.
>
> Exemplo:
>
>     ** Jogo da Forca **
>     Palavra: __________
>     Adivinhe a letra: a
>     Acertou!
>
>     Palavra: _a_a__a_a_
>     Adivinhe a letra: e
>     Errou! 
>     Tentativas restantes: 4
>
>     Palavra: _a_a__a_a_
>     Adivinhe a letra: i
>     Acertou!
>
>     Palavra: _a_a__aia_
>     Adivinhe a letra: s
>     Acertou!
>
>     Palavra: sa_a__aias
>     Adivinhe a letra: m
>     Acertou!
>
>     Palavra: samam_aias
>     Adivinhe a letra: b
>     Acertou!
>
>     Você ganhou!
>     A palavra era samambaias.
>
> Implemente também as seguintes funcionalidades:
> * Crie uma lista de palavras ocultas e escolha uma aleatoriamente quando o jogo começa.
> * Se o usuário escolher uma letra já escolhida anteriormente, peça novamente.
>
> ***