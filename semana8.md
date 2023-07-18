# PI - Semana 8

## Matrizes

Uma matriz é uma arranjo de valores dispostos em linhas e colunas, como em uma tabela.

Veja a seguir uma matriz de números inteiros. O **tamanho da matriz** é 4x3, pois os valores estão dispostos em 4 linhas e 3 colunas:

```
10    5   -2
 7   -1   21
61   42    0
 9    2   -1
```

A seguir temos uma matriz de tamanho 2x2 (2 linhas e 2 colunas):

```
-5   2
 0   1
```

E, agora, uma matriz 1x5 (1 linha e 5 colunas):

```
8   -3   10   6   29
```

Python não tem um tipo de dado embutido para representar matrizes. Não há, por exemplo, um tipo de dado `matrix` pronto para usar. Entretanto, podemos facilmente simular o comportamento de uma matriz através de "listas de listas", isto é, criando uma lista que contém outras listas.

Observe novamente o primeiro exemplo de matriz (matriz 4x3):

```
10    5   -2
 7   -1   21
61   42    0
 9    2   -1
```

Podemos supor que cada linha da matriz é uma lista em Python:


```python
[10,  5,  -2]
[ 7, -1,  21]
[61, 42,   0]
[ 9,  2,  -1]
```

Agora, criamos uma lista `m` que contém essas 4 listas:

```python
m = [[10,  5,  -2],
     [ 7, -1,  21],
     [61, 42,   0],
     [ 9,  2,  -1]]
```

Se observarmos o conteúdo de `m` no REPL, veremos o seguinte:

```
>>> m
[[10, 5, -2], [7, -1, 21], [61, 42, 0], [9, 2, -1]]
```

Podemos interpretar `m` como uma matriz organizada como uma "lista de linhas": 

* `m[0]` é o conteúdo da primeira linha da matriz, `[10, 5, -2]`,
* `m[1]` é o conteúdo da segunda linha da matriz, `[7, -1, 21]`,
* e assim por diante...

O número de linhas da matriz é `len(m)`.

Podemos indexar o conteúdo de cada linha da matriz. Por exemplo:

* `m[0][0]` é o elemento da primeira linha, primeira coluna, isto é, `10`,
* `m[0][1]` é o elemento da primeira linha, segunda coluna, isto é, `5`,
* `m[0][2]` é o elemento da primeira linha, terceira coluna, isto é, `-2`,
* `m[1][0]` é o elemento da segunda linha, primeira coluna, isto é, `7`,
* `m[1][1]` é o elemento da segunda linha, segunda coluna, isto é, `-1`,
* `m[1][2]` é o elemento da segunda linha, terceira coluna, isto é, `21`,
* e assim por diante...

Em resumo, `m[i][j]` corresponde ao elemento da linha `i` e coluna `j` da matriz.

> **Observação:** tanto `i` quanto `j` começam a partir de `0` e terminam no tamanho da lista menos 1. Assim, em uma matriz 4x3:
> * `m[0][0]` é o elemento da primeira linha, primeira coluna;
> * `m[3][2]`  o elemento da última linha, última coluna.
>
> ***

Para que `m` seja considerada uma matriz, vamos considerar que todas as linhas devem ter o mesmo número de colunas. Segundo essa regra, a variável `x` a seguir não é uma matriz

```
x = [[10,  5,  -2],
     [ 7, -1,  21],
     [61, 42],
     [ 9,  2,  -1]]
```

pois `len(x[2])` é `2`, mas todas as outras linhas têm tamanho 3.

> **Observação:** até agora convencionamos que uma matriz é uma "lista de linhas". De forma alternativa, podemos organizar uma matriz como uma "lista de colunas". Nesse caso, o elemento da linha `i` e coluna `j` será acessado com `m[j][i]` ao invés de `m[i][j]`. Considere novamente a matriz do exemplo anterior:
> ```
> 10    5   -2
>  7   -1   21
> 61   42    0
>  9    2   -1
> ```
> Para criar uma "lista de colunas", fazemos assim:
>
> ```python
> m = [[10,  7,  61,  9],
>      [ 5, -1,  42,  2],
>      [-2, 21,   0, -1]]
> ```
> Agora, `m[0]` é uma lista com os elementos da primeira coluna da matriz; `m[1]` contém os elementos da segunda coluna, e assim por diante.
>
> Ainda que uma matriz como "lista de colunas" possa ser útil para acessar rapidamente todos os elementos de cada coluna, nos exercícios a seguir vamos considerar que uma matriz é sempre uma "lista de linhas".
>
> ***

> **Exercício 8.1 - Verificando se `m` é uma matriz**
>
> Faça uma função `verifica_matriz(m)` que retorna `True` se `m` é uma matriz, e `False` caso contrário.
>
> Suponha que `m` é uma lista de listas (linhas da matriz) e que a matriz tem pelo menos uma linha. `m` é uma matriz se todas as linhas têm o mesmo número de colunas.
>
> Exemplos:
> * `verifica_matriz([[3, 2], [-3, 4]])` é `True`.
> * `verifica_matriz([[3, 2], [-3, 4], [5, 0]])` é `True`.
> * `verifica_matriz([[1], [2], [3]])` é `True`.
> * `verifica_matriz([[1, 2, 3]])` é `True`.
> * `verifica_matriz([[3, 2], [-3, 4], [5]])` é `False`.
>
> ***

> **Exercício 8.2 - Tamanho da matriz**
>
> Faça uma função `tamanho_matriz(mat)` que recebe uma matriz `mat` e retorna o número de linhas e colunas. Considere que `mat` é uma lista de listas (linhas da matriz) e que a matriz tem pelo menos uma linha.
>
> A função pode retornar o número de linhas e colunas da seguinte forma:
>
> ```python
> def tamanho_matriz(mat):
>   # Complete o código aqui
>   # ...
>   return num_linhas, num_colunas
>
> # Chamando a função
> l, c = tamanho_matriz([[3, 2], [-3, 4], [5,0]])
> print("Número de linhas:", l) # 3
> print("Número de colunas:", c) # 2
> ```
>
> ***

> **Exercício 8.3 - Matriz identidade**
>
> Uma **matriz identidade** é uma matriz na qual todos os elementos são `0`, exceto os elementos da _diagonal principal_, que são `1`. Os elementos da **diagonal principal** de uma matriz são aqueles em que `i==j`, onde `i` e `j` são o número da linha e coluna do elemento. Por exemplo, a matriz a seguir é uma matriz identidade:
>
> ```python
> mat = [[1, 0, 0, 0],
>        [0, 1, 0, 0],
>        [0, 0, 1, 0],
>        [0, 0, 0, 1]]
> ```
>
> Uma matriz identidade é sempre uma **matriz quadrada**, isto é, uma matriz na qual o número de linhas é igual ao número de colunas.
> 
> Faça uma função `matriz_identidade(n)` que recebe um inteiro positivo `n` e retorna uma matriz identidade de tamanho _n_ x _n_. Por exemplo:
>
> * `matriz_identidade(4)` retorna a matriz do exemplo acima. 
> * `matriz_identidade(1)` retorna a matriz `[[1]]`.
>
> ***

> **Exercício 8.4 - Soma das linhas da matriz**
>
> Faça uma função `somar_linhas(mat)` que recebe uma matriz `mat` de tamanho _m_ x _n_ e retorna uma lista de tamanho _m_ contendo a soma dos elementos de cada linha da matriz.
>
> Por exemplo, se `mat` é a seguinte matriz:
>
> ```python
> mat = [[10,  5,  -2],
>        [ 7, -1,  21],
>        [61, 42,   0],
>        [ 9,  2,  -1]]
> ```
> Então, `somar_linhas(mat)` deverá retornar `[13, 27, 103, 10]`.
>
> ***

> **Exercício 8.5 - Soma das colunas da matriz**
>
> Faça uma função `somar_colunas(mat)` que recebe uma matriz `mat` de tamanho _m_ x _n_ e retorna uma lista de tamanho _n_ contendo a soma dos elementos de cada coluna da matriz.
>
> Por exemplo, se `mat` é a seguinte matriz:
>
> ```python
> mat = [[10,  5,  -2],
>        [ 7, -1,  21],
>        [61, 42,   0],
>        [ 9,  2,  -1]]
> ```
> Então, `somar_colunas(mat)` deverá retornar `[87, 48, 18]`.
>
> ***

> **Exercício 8.6 - Quadrado mágico**
>
> Faça uma função `quadrado_magico(mat)` que recebe uma matriz `mat` de tamanho _n_ x _n_ e retorna `True` se `mat` é um **quadrado mágico**. Um quadrado mágico é uma matriz na qual a soma dos elementos em cada linha, cada coluna, e em ambas as diagonais, é o mesmo valor.
>
> Por exemplo, se `mat` é a seguinte matriz:
>
> ```python
> mat = [[2, 7, 6],
>        [9, 5, 1],
>        [4, 3, 8]]
> ```
> Então, `quadrado_magico(mat)` deverá retornar `True` pois a soma de cada linha, coluna e diagonal é 15.
>
> ***

> **Exercício 8.7 - Índice do maior elemento da matriz**
>
> Faça uma função `indice_do_maximo(mat)` que recebe uma matriz `mat` de inteiros e retorna um par (`i`, `j`) que corresponde ao índice do maior elemento da matriz.
>
> Por exemplo, se `mat` é a seguinte matriz:
>
> ```python
> mat = [[10,  5,  -2],
>        [ 7, -1,  21],
>        [61, 42,   0],
>        [ 9,  2,  -1]]
> ``` 
> Então, em `i, j = indice_do_maximo(mat)`, `i` será `2` e `j` será `0`, pois `mat[2][0]` contém o maior elemento (`61`).
>
> ***

> **Exercício 8.8 - Linha e coluna igual (versão 1)**
>
> Faça uma função `linha_coluna_igual1(mat)` que recebe uma matriz `mat` de tamanho _n_ x _n_ e retorna `True` se existe alguma linha que seja igual a alguma coluna.
>
> Por exemplo, se `mat` é a seguinte matriz:
>
> ```python
> mat = [[ 9, -8,  3],
>        [-8, -1,  21],
>        [ 3,  7,  9]]
> ``` 
> Então, `linha_coluna_igual1(mat)` é `True` pois a primeira linha é igual à primeira coluna.
>
> ***


> **Exercício 8.9 - Linha e coluna igual (versão 2: fora de ordem)**
>
> No exercício anterior, uma linha e coluna são consideradas iguais apenas se os elementos aparecem na mesma ordem. Neste exercício, considere que a ordem dos elementos não importa. Basta que a linha e a coluna tenham os mesmos elementos, em qualquer ordem.
>
> Por exemplo, se `mat` é a seguinte matriz:
>
> ```python
> mat = [[ 9, -8,  3],
>        [ 5, -1,  9],
>        [ 0,  7, -8]]
> ``` 
> Então, `linha_coluna_igual2(mat)` é `True` pois os elementos da primeira linha também estão na última coluna (ainda que em uma ordem diferente).
>
> ***