
1. Manipulação de Strings
Você pode usar métodos para manipular dados de texto em colunas.

# Converte todas as strings de uma coluna para minúsculas
df['Coluna1'] = df['Coluna1'].str.lower()

# Remove espaços em branco no início e no final das strings
df['Coluna1'] = df['Coluna1'].str.strip()

# Substitui parte de uma string por outra
df['Coluna1'] = df['Coluna1'].str.replace('Antigo', 'Novo')


2. Agrupamento de Dados (groupby)
Agrupa dados com base em uma ou mais colunas e aplica funções agregadas, como soma, média, contagem, etc.

# Agrupa os dados por uma coluna e calcula a média de outra coluna
df_agrupado = df.groupby('ColunaAgrupamento')['ColunaValores'].mean()

# Agrupa por várias colunas e conta as ocorrências
df_contagem = df.groupby(['Coluna1', 'Coluna2']).size().reset_index(name='Contagem')


3. Merge e Join
Combina diferentes DataFrames usando chaves comuns.

# Mescla dois DataFrames com base em uma coluna comum
df_merged = pd.merge(df1, df2, on='ColunaComum')

# Faz uma junção à esquerda entre dois DataFrames
df_left_join = pd.merge(df1, df2, how='left', on='ColunaComum')


4. Pivot e Unpivot (pivot, melt)
Transforma dados de formato longo para largo e vice-versa.

# Pivota os dados para transformar colunas em valores de uma nova coluna
df_pivot = df.pivot(index='Coluna1', columns='Coluna2', values='Coluna3')

# Derrete (unpivot) os dados para transformar colunas em linhas
df_melt = df.melt(id_vars=['Coluna1'], value_vars=['Coluna2', 'Coluna3'])


5. Tratamento de Outliers
Você pode identificar e tratar outliers, que são valores anômalos nos dados.

# Identifica outliers usando o desvio padrão
desvio = 3
outliers = df[df['Coluna1'] > df['Coluna1'].mean() + desvio * df['Coluna1'].std()]

# Remove outliers da coluna
df_sem_outliers = df[df['Coluna1'] <= df['Coluna1'].mean() + desvio * df['Coluna1'].std()]


6. Filtragem de Dados
Filtra os dados com base em condições específicas.

# Filtra as linhas onde os valores da coluna são maiores que um certo valor
df_filtrado = df[df['Coluna1'] > 100]

# Filtra com base em múltiplas condições
df_filtrado_multicondicoes = df[(df['Coluna1'] > 100) & (df['Coluna2'] == 'Valor')]


7. Interpolação
Preenche valores faltantes (nulos) com base em uma interpolação.
# Interpola valores nulos linearmente
df_interpolado = df.interpolate(method='linear')


8. Data Transformation (Transformação de Dados)
Transforma os dados de acordo com uma função customizada.

# Aplica uma transformação logarítmica em uma coluna
df['Coluna_log'] = df['Coluna1'].apply(np.log)


9. Uso de Bibliotecas Externas

from sklearn.preprocessing import StandardScaler

# Normaliza os dados com StandardScaler
scaler = StandardScaler()
df[['Coluna1_normalizada']] = scaler.fit_transform(df[['Coluna1']])


10. Manipulação de Datas
Trabalhe com dados de tempo utilizando funções específicas de Pandas.

# Converte uma coluna para o tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

# Extrai o ano de uma coluna de data
df['Ano'] = df['Data'].dt.year

# Filtra dados de um período específico
df_filtrado_data = df[(df['Data'] >= '2023-01-01') & (df['Data'] <= '2023-12-31')]