import streamlit as st

# Título do aplicativo
st.title('Meu Primeiro Aplicativo Streamlit')

# Adicionando um texto
st.write('Bem-vindo ao meu aplicativo!')

# Adicionando um gráfico
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

#data = pd.DataFrame(np.random.randn(100, 2), columns=['x', 'y'])
#st.line_chart(data)

# Adicionando um controle de entrada
user_input = st.text_input("Digite seu nome:")
st.write('Olá, ', user_input, '!')

# Exibindo uma tabela
#st.write(data)
