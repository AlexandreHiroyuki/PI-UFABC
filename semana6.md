# PI - Semana 6

## Listas

Em programação, uma **lista** (ou **vetor**) é uma sequência de valores identificadas por uma única variável.

Por exemplo, podemos criar uma lista de nome `lst` para armazenar 10 números inteiros. Para fazer isso em Python, usamos colchetes e colocamos os elementos da lista separados por vírgula:

```python
# Criando uma lista de 10 inteiros
lst = [10, 5, -4, 7, 21, 3, 3, 9, 42, 0]
```

O tipo de dado da variável `lst` é `list`. Veja no REPL:

```
>>> type(lst)
<class 'list'>
```

Os elementos da lista podem ser acessados através de **indexação** usando a sintaxe `nome[indice]`, onde `nome` é o nome da lista, e `indice` é um inteiro entre `0` e o número de elementos da lista menos 1. Veja alguns exemplos de acesso indexado a elementos da lista anterior:


```
>>> lst[0]
10
>>> lst[4]
21
>>> lst[9]
0
```
`lst[0]` é o primeiro elemento, `lst[1]` é o segundo elemento, e assim por diante.


A expressão `nome[indice]` pode ser usada como se fosse o nome de uma variável e pode inclusive ter seu valor modificado:

```
>>> lst[0] = 10
>>> lst[1] = lst[0] * 2
>>> lst
[10, 20, -4, 7, 21, 3, 3, 9, 42, 0]
>>> type(lst[0])
<class 'int'>
```

Ao contrário de outras linguagens de programação, em Python os elementos da lista não precisam ser todos do mesmo tipo. Podemos, por exemplo, misturar `int` com `str` e `bool` em uma mesma lista:

```
>>> lst[0] = True
>>> lst[1] = "Vinte"
>>> lst
[True, 'Vinte', -4, 7, 21, 3, 3, 9, 42, 0]
```

## Tamanho da lista

O tamanho de uma lista é o número de elementos dentro da lista. O tamanho é obtido com a função embutida `len()`:

```
>>> x=[20, 5.2, False, "UFABC"]
>>> len(x)
4
```

## Diferentes formas de criar uma lista

Já vimos que podemos criar uma lista ao escrever valores separados por vírgula dentro de um par de colchetes. Entretanto, também podemos criar uma **lista vazia**. Para isso bastar usar `[]`:

```
>>> vazio=[]
>>> len(vazio)
0
```

Uma lista também pode ser criada com a função `list()`. Se nenhum argumento for passado para a função, o resultado será uma lista vazia. Para criar uma lista não vazia, os valores devem ser escritos dentro de um par extra de parênteses (uma _tupla_ de valores):

```
>>> list((42, True, "Olá"))
[42, True, 'Olá']
```

A função `list()` também pode ser usada para converter uma string em uma lista:

```
>>> list("UFABC")
['U', 'F', 'A', 'B', 'C']
```

> **Observação:** para o caminho inverso, isto é, para converter uma lista de strings em uma única string, podemos usar `''.join(nome_da_lista)`:
>
> ```
> >>> x = list("UFABC")
> >>> x
> ['U', 'F', 'A', 'B', 'C']
> >>> y = ''.join(x)
> >>> y
> 'UFABC'
> ```
> Entre as aspas (logo antes do `join`) é possível colocar um caractere/string de separação. Por exemplo, `'-'.join(x)` resultará em `"U-F-A-B-C"`.
>
> A propósito, também podemos indexar strings da mesma forma que indexamos listas. Por exemplo, se `y` é a string `"UFABC"`, `y[0]` é a letra `U`, `y[1]` é a letra `F`, etc.
>
> Outra função útil para converter strings em uma lista é `str.split(separador)`, onde `str` é a string que queremos converter em lista, e `separador` é uma string opcional que especifica o caractere/string de separação (o padrão é o caractere de espaço). Veja um exemplo:
>
> ```
> >>> x="Universidade Federal do ABC"
> >>> x.split()
> ['Universidade', 'Federal', 'do', 'ABC']
> >>> x.split('e')
> ['Univ', 'rsidad', ' F', 'd', 'ral do ABC']
> ```
> ***

Para criar uma lista com vários elementos replicados podemos usar o operador `*`. Veja o exemplo a seguir que cria uma lista de 10 zeros:

```
>>> [0] * 10
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

Também podemos criar uma nova lista através da concatenação de outras listas, usando o operador `+`:

```
>>> [10, 20] + [30, 40]
[10, 20, 30, 40]
```

## Adicionando elementos em uma lista

O operador de concatenação (`+`) pode ser utilizado para adicionar um elemento no final de uma lista já existente.

O exemplo a seguir mostra como o valor de `y` (um `int`) pode ser adicionado ao final da lista `x`:

```
>>> x=[5, 10, 2]
>>> y=3
>>> x=x+[y]
>>> x
[5, 10, 2, 3]
```

Note que `x=x+y` não funciona no lugar de `x=x+[y]`. Só é possível concatenar `list` com `list`. Não é possível concatenar `list` com `int`.

Ainda uma outra forma de adicionar um elemento ao final de uma lista é através da função `append(valor)`, onde `valor` é o valor que queremos adicionar. Essa função faz parte do tipo de dado `list` e por isso deve ser prefixada com o nome da lista. Veja um exemplo:

```
>>> x=[5, 10, 2]
>>> y=3
>>> x.append(y)
>>> x
[5, 10, 2, 3]
```

> Funções que fazem parte de um tipo de dado, como `append`, são comumente chamadas de **métodos**. 

## Inserindo elementos em uma lista

Para inserir um novo elemento no meio de uma lista podemos usar o método `insert(indice, valor)`, onde `indice` é o índice que o novo valor irá ocupar na lista, e `valor` é o valor que queremos inserir. Os elementos a partir de `indice` são deslocados à direita para dar espaço ao novo valor.

```
>>> x=["Universidade", "Federal", "ABC"]
>>> x.insert(2, "do")
>>> x
['Universidade', 'Federal', 'do', 'ABC']
```

## Removendo elementos de uma lista

O método `remove(valor)` remove o primeiro elemento da lista que valor igual a `valor`.

```
>>> x=[5, 10, 2, 3]
>>> x.remove(10)
>>> x
[5, 2, 3]
```

O método `pop(indice)` remove o elemento de índice `indice` e retorna o valor removido. Se `indice` não for especificado, o elemento removido será o último da lista.

```
>>> x=[5, 10, 2, 3]
>>> x.pop(1)
10
>>> x
[5, 2, 3]
```

Outra forma de remover um elemento (dado um índice) é usando a palavra reservada `del`:

```
>>> x=[5, 10, 2, 3]
>>> del x[1]
>>> x
[5, 2, 3]
```

## Indexação negativa

Em Python, podemos usar números negativos para indexar uma lista:

* O elemento de índice `-1` é o último elemento da lista,
* o elemento de índice `-2` é o penúltimo elemento da lista,
* e assim por diante...

Exemplo:

```
>>> x=[5, 10, 2]
>>> x[-1]
2
>>> x[-2]
10
```

## Acessando intervalos de uma lista

Podemos acessar um intervalo `[inicio, fim)` (intervalo fechado à esquerda e aberto à direita) de índices de uma lista através da sintaxe `nome[inicio:fim]` ou `nome[inicio:fim:passo]`, onde:

* `inicio` é o índice inicial (fechado);
* `fim` é o índice final (aberto);
* `passo` é o tamanho do passo (1 caso não seja especificado).

Exemplos:
```
>>> x=[5, 10, 2, 3, 7, -1]
>>> x[1:3]
[10, 2]
>>> x[0:len(x):2]
[5, 2, 7]
>>> 
```

## Copiando listas

Se criarmos uma lista `a` e então fizermos `b = a` (atribuição de `a` em `b`), `b` não será uma cópia de `a`, como seria esperado. A princípio até pode parecer uma cópia, mas não é. Veja o exemplo a seguir:

```
>>> a=[5, 10, 2, 3]
>>> b=a
>>> b
[5, 10, 2, 3]
```

Parece que `b` é uma cópia de `a`. Mas veja o que acontece com `b` quando modificamos algum elemento de `a`:

```
>>> a[0]=42
>>> a
[42, 10, 2, 3]
>>> b
[42, 10, 2, 3]
```

O primeiro elemento de `b` também foi modificado! Isso ocorre pois `b` é uma _referência_ à `a`. Em outras palavras, tudo o que acontece com `a` também acontece com `b`. De fato, `a` e `b` são apenas nomes diferentes que se referem à mesma sequência de valores na memória. Esse comportamento também ocorre quando passamos uma lista como argumento de uma função.

Se quisermos realmente copiar uma lista, isto é, criar um clone da lista, podemos usar o método `copy()`:

```
>>> b = a.copy()
```

Podemos também usar a função `list()`:

```
>>> b = list(a)
```

Para saber se `a` e `b` se referem a uma mesma lista, podemos avaliar a expressão `a is b`. O resultado é `True` se `a` e `b` se referem ao mesmo objeto, e `False` caso contrário:

```
>>> a=[5, 10, 2, 3]
>>> b=a
>>> a is b
True
>>> b=a.copy()
>>> a is b
False
```

## Iterando sobre uma lista

Com o uso de indexação podemos fazer um laço `for` que visita os elementos de uma lista. O exemplo a seguir itera sobre os elementos de uma lista `x`, mostrando cada elemento na tela com o `print()`:

```python
x = [5, 10, 2, 3]
for i in range(len(x)):
    print(x[i])
```

Uma sintaxe mais simples para iterar sobre uma lista é mostrada a seguir:

```python
x = [5, 10, 2, 3]
for elem in x:
    print(elem)
```

Neste exemplo, `elem` é o elemento da lista que está sendo visitado em cada iteração.

## Compreensão de lista

Uma forma ao mesmo tempo concisa e flexível de criar listas em Python é através do uso de **compreensão de lista**.

Veja um primeiro exemplo a seguir que cria uma lista `y` que contém os elementos da lista `x` elevados ao quadrado:

```
>>> x = [5, 10, 2, 3]
>>> y = [elem**2 for elem in x]
>>> y
[25, 100, 4, 9]
```

A expressão `[elem**2 for elem in x]` pode ser lida como "crie uma lista composta de valores `elem**2`, onde `elem` é cada elemento de `x`".

O `for` na compreensão de lista também pode iterar sobre um `range`, como no exemplo a seguir:

```
>>> y = [i+1 for i in range(10)]
>>> y
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

A expressão `[i+1 for i in range(10)]` pode ser lida como "crie uma lista composta de valores `i+1`, onde `i` é cada elemento de um `range(10)`".

Opcionalmente, é possível colocar uma condição depois do `for` para filtrar valores do laço. O exemplo a seguir usa uma condição para considerar apenas os valores `i` que são pares:

```
>>> y = [i+1 for i in range(10) if i%2 == 0]
>>> y
[1, 3, 5, 7, 9]
```

A expressão `[i+1 for i in range(10) if i%2 == 0]` pode ser lida como "crie uma lista composta de valores `i+1`, onde `i` é cada elemento de um `range(10)` para o qual a expressão `i%2 == 0` é `True`":
 
1. `i+1` é uma **expressão** que resulta no valor de **saída**;
2. `for i in range(10)` é a **coleção** que está sendo iterada;
3. `if i%2 == 0` é a **condição** que precisa ser satisfeita para que o valor iterado seja usado na saída.

É possível criar o vetor `y` sem usar compreensão de lista, mas para isso precisamos de várias linhas de código:

```python
# O código a seguir faz a mesma coisa que
# y = [i+1 for i in range(10) if i%2 == 0]
y = []
for i in range(10):
    if i % 2 == 0:
        y += [i + 1]
```

## Outros métodos de `list`

Método        | Descrição
:-----        | :-----    
`clear()`     | Remove todos os elementos da lista.
`count(valor)`| Retorna a quantidade de elementos com o valor `valor`.
`index(valor)`| Retorna o índice da primeira ocorrência do valor `valor`.
`reverse()`   | Reverte a ordem os elementos da lista.
`sort()`      | Ordena a lista em ordem crescente.

> **Exercício 6.1 - Média de notas**
>
> Faça um programa que cria uma lista `notas` de notas de uma turma de `n` alunos e no final imprime a lista e a média das notas. O valor `n` e as notas devem ser entrados pelo usuário.
>
> Exemplos de execução:
>
>     Digite o número de notas: 5
>     7
>     8
>     4
>     10
>     9
>     Lista: [7, 8, 4, 10, 9]
>     Média: 7.6
>
> ***

> **Exercício 6.2 - Classificação por média**
>
> Faça uma função `classificar_notas(v)` que recebe uma lista `v` de notas e retorna uma lista de mesmo tamanho que `v`, mas contendo as palavras `"abaixo"` e `"acima"` de acordo com a classificação de cada nota em relação à média (se a nota for exatamente igual à média, classifique como `"acima"`).
>
> Por exemplo, se a lista de notas é `v = [7, 8, 4, 10, 9]` então `classificar_notas(v)` deve retornar `["abaixo", "acima", "abaixo", "acima", "acima"]`.
>
> ***

> **Exercício 6.3 - Número de ocorrências**
>
> Faça uma função `ocorrencias(valor, lista)` que retorna o número de vezes em que o valor `valor` aparece na lista `lista`. Esse exercício pode ser resolvido facilmente com `lista.count(valor)`. Entretanto, você deve fazer sua solução sem usar o método `count`. 
>
> ***

> **Exercício 6.4 - Números próximos**
>
> Faça uma função `proximos(valor, margem, lista)` que retorna o número de vezes que valores no intervalo `[valor-margem, valor+margem]` aparecem na lista de números `lista`. Considere que os valores são todos `int`, e `margem >= 0.0`.
>
> ***

> **Exercício 6.5 - Histograma**
>
> Faça uma função `histograma(v)` que recebe uma lista de inteiros no intervalo `[0, 9]`. A função deve retornar uma nova lista de tamanho 10 contendo a quantidade de ocorrências dos valores de 0 a 9 em `v`. Por exemplo, no índice 5 da lista retornada deverá ter a quantidade de números 5 encontrados em `v`.
>
> ***

> **Exercício 6.6 - Ordenação**
>
> Faça uma função `ordenado(v)` que recebe uma lista de números `v` e retorna uma nova lista com os valores de `v` ordenados. Não use o método `sort()`. Há diversos algoritmos de ordenação, mas um bastante simples consiste nos seguintes passos:
> 1. Crie uma lista vazia `res` que vai conter o resultado.
> 2. Retire o menor elemento de `v` e adicione em `res`.
> 3. Repita o passo 2 até esvaziar `v`.
> 4. Retorne `res`.
>
> ***

> **Exercício 6.7 - Removendo caracteres**
>
> Faça uma função `remove_caractere(texto, caractere)` que recebe uma string `texto` e uma string `caractere` de apenas 1 caractere, e remove todas as ocorrências do caractere `caractere` em `texto`. A função deve retornar a string modificada.
>
> Por exemplo:
> * `remove_caractere("papagaio", "a")` deverá retornar `"ppgio"`.
> * `remove_caractere("computador", "i")` deverá retornar `"computador"`.
>
> ***

> **Exercício 6.8 - Número de dígitos**
>
> Faça uma função `contar_digitos(texto)` que retorna quantos dígitos (caracteres de `0` a `9`) existem na string `texto`.
>
> Por exemplo:
> * `contar_digitos("j90s1mkj34")` deverá retornar `5`.
> * `contar_digitos("01216640")` deverá retornar `8`.
> * `contar_digitos("iwexlk")` deverá retornar `0`.
>
> ***

> **Exercício 6.9 - Cartão de cŕedito**
>
> Faça uma função `luhn(num_cartao)`, que verifica se um dado número de cartão de crédito é válido de acordo com o "algoritmo de Luhn". O algoritmo de Luhn é o algoritmo utilizado para validar números de cartão de crédito. O parâmetro `num_cartao` é uma string no formato `XXXX XXXX XXXX XXXX` onde `X` é um dígito.
>
> Veja como implementar o algoritmo de Luhn:
> 1. Dobre o valor do segundo e do quarto dígito de cada grupo `XXXX`.
> 2. Se o valor dobrado for maior que 9, subtraia 9 do resultado.
> 3. Some todos os dígitos.
> 4. Se a soma for divisível por 10, o número é válido.
>
> Por exemplo:
> * `luhn("4539 3195 0343 6467")` deverá retornar `True`.
> * `luhn("8273 1232 7352 0569")` deverá retornar `False`.
>
> ***

> **Exercício 6.10 - Distância de Hamming**
>
> Faça uma função `hamming(a, b)`, que calcula a distância de Hamming de duas strings `a` e `b` de mesmo tamanho.
>
> ***

> **Exercício 6.11 - Isograma**
>
>
> ***

> **Exercício 6.12 - ISBN**
>
>
> ***