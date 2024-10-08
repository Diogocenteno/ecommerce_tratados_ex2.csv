import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Carregar os dados
df = pd.read_csv('/data/ecommerce_tratados_ex2.csv')

# Verificar os nomes das colunas
print(df.columns)

# Inicializar os scalers
scaler = MinMaxScaler()
label_encoder = LabelEncoder()

# Transformações com MinMaxScaler (use os nomes corretos)
df['Nota_MinMax'] = scaler.fit_transform(df[['Nota']])
df['N_Avaliações_MinMax'] = scaler.fit_transform(df[['N_Avaliações']])  # ajuste conforme necessário
df['Desconto_MinMax'] = scaler.fit_transform(df[['Desconto']])
df['Preco_MinMax'] = scaler.fit_transform(df[['Preco']])

# Transformações com LabelEncoder
df['Marca_Cod'] = label_encoder.fit_transform(df['Marca'])
df['Material_Cod'] = label_encoder.fit_transform(df['Material'])
df['Temporada_Cod'] = label_encoder.fit_transform(df['Temporada'])
