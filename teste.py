import plotly.express as px
import pandas as pd

# Criando dados de exemplo
data = {
    'Categorias': ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D'],
    'Valores': [450, 250, 150, 300]
}

data = {
    'Categorias': ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D'],
    'Valores': [6100, 2540, 15550, 3500]
}


# Convertendo para DataFrame
df = pd.DataFrame(data)

# Criando o gráfico de barras
fig = px.bar(df, x='Categorias', y='Valores', title='Gráfico de Barras - Categorias e Valores')
fig2 = px.bar(df, x='Categorias', y='Valores', title='Gráfico de Barras - Categorias e Valores')


# Exibindo o gráfico
fig.show()
fig2.show()
