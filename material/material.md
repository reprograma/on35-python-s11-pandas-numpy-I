

### 1. `read_csv()`
A função `read_csv()` é usada para ler um arquivo CSV e convertê-lo em um DataFrame do pandas.

```python
import pandas as pd

# Lê o arquivo CSV e cria um DataFrame
df = pd.read_csv('caminho/para/seu_arquivo.csv')
df = pd.read_csv('seu_arquivo.csv', delimiter=';', skiprows=8)
```

### 2. `head()`
Exibe as primeiras linhas do DataFrame. Por padrão, mostra as 5 primeiras linhas.

```python
# Exibe as 5 primeiras linhas
print(df.head())

# Exibe as 10 primeiras linhas
print(df.head(10))
```

### 3. `tail()`
Exibe as últimas linhas do DataFrame. Por padrão, mostra as 5 últimas linhas.

```python
# Exibe as 5 últimas linhas
print(df.tail())

# Exibe as 10 últimas linhas
print(df.tail(10))
```

### 4. `shape`
Retorna a quantidade de linhas e colunas do DataFrame em formato de tupla `(linhas, colunas)`.

```python
# Exibe o formato do DataFrame
print(df.shape)
```

### 5. `describe()`
Gera estatísticas descritivas para colunas numéricas, como contagem, média, desvio padrão, valores mínimo e máximo, e quartis.

```python
# Exibe estatísticas descritivas
print(df.describe())
```

### 6. `dtypes`
Retorna os tipos de dados de cada coluna no DataFrame.

```python
# Exibe os tipos de dados das colunas
print(df.dtypes)
```

### 7. `sample()` e `reset_index()`
- `sample()`: Seleciona uma amostra aleatória de linhas do DataFrame.
- `reset_index()`: Reseta o índice do DataFrame, útil após filtragens ou amostragens.

```python
# Seleciona 5 linhas aleatórias
amostra = df.sample(n=5)

# Reseta o índice do DataFrame amostrado
amostra_resetada = amostra.reset_index(drop=True)

print(amostra_resetada)
```

### 8. Reduzir o DataFrame
Selecionar um subconjunto de colunas e/ou linhas.

```python
# Selecionar 3 colunas específicas
df_reduzido = df[['Coluna1', 'Coluna2', 'Coluna3']]

df_reduzido.head()

# Selecionar 1000 linhas aleatórias
df_reduzido = df_reduzido.sample(n=1000, random_state=42)
```

### 9. `columns`
Exibe ou altera os nomes das colunas.

```python
# Exibe os nomes das colunas
print(df.columns)

# Altera os nomes das colunas
df.columns = ['NovoNome1', 'NovoNome2', 'NovoNome3']
```

### 10. Selecionar uma coluna
Você pode selecionar uma coluna específica utilizando a notação de colchetes.

```python
# Seleciona a coluna 'Coluna1'
coluna1 = df['Coluna1']
print(coluna1)
```

### 11. `min()`, `max()`, `sum()` e `mean()`
Funções para calcular o valor mínimo, máximo, soma e média, respectivamente.

```python
# Valor mínimo
minimo = df['Coluna1'].min()

# Valor máximo
maximo = df['Coluna1'].max()

# Soma dos valores
soma = df['Coluna1'].sum()

# Média dos valores
media = df['Coluna1'].mean()

print(f"Mínimo: {minimo}, Máximo: {maximo}, Soma: {soma}, Média: {media}")
```

### 12. `isnull()`
Identifica valores nulos no DataFrame, retornando um DataFrame booleano.

```python
# Verifica valores nulos
nulos = df.isnull()
print(nulos)

#numeros nulos
df.isnull().sum()

# Contagem de valores nulos em cada coluna
nulos_por_coluna = df.isnull().sum()
print(nulos_por_coluna)
```

### 13. `dropna()`
Remove linhas ou colunas que contenham valores nulos.

```python
# Remove linhas com qualquer valor nulo
df_sem_nulos = df.dropna()

# Remove colunas que contenham valores nulos
df_sem_nulos_colunas = df.dropna(axis=1)

# Remover coluna valores
df_sem_nulo = df.dropna(subset=['nome da coluna'])
```

# Remover 

remover = df.dropna(axis=0, how='all')
remover


### 14. `fillna()`
Preenche valores nulos com um valor específico.

```python
# Preenche valores nulos com 0
df_preenchido = df.fillna(0)

# Preenche valores nulos com a média da coluna
df_preenchido_media = df.fillna(df.mean())
```

### 15. `replace()`
Substitui valores específicos no DataFrame.

```python
# Substitui todos os valores 0 por NaN
df_substituido = df.replace(0, -1)

# Substitui um valor específico em uma coluna
df['Coluna1'] = df['Coluna1'].replace('ValorAntigo', 'ValorNovo')
```
df_substituido.head(9)

### 16. `drop_duplicates()`
Remove linhas duplicadas do DataFrame.

```python
# Remove linhas duplicadas
df_sem_duplicatas = df.drop_duplicates()

# Remove duplicatas com base em colunas específicas
df_sem_duplicatas_colunas = df.drop_duplicates(subset=['Coluna1', 'Coluna2'])
```

### 17. Normalização
A normalização é o processo de ajustar os valores das colunas para um mesmo intervalo, geralmente entre 0 e 1.

```python
# Normaliza os valores de uma coluna para o intervalo [0, 1]
df['Coluna1_normalizada'] = (df['Coluna1'] - df['Coluna1'].min()) / (df['Coluna1'].max() - df['Coluna1'].min())

# Outra forma de normalização usando o método z-score (normalização padrão)
df['Coluna1_zscore'] = (df['Coluna1'] - df['Coluna1'].mean()) / df['Coluna1'].std()
```

# coluna_temperatura_maxima = pd.to_numeric(df('TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)'), errors='coerce')
# coluna_temperatura_maxima = pd.to_numeric(df['TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)'], errors='coerce')

# pip install matplotlib

