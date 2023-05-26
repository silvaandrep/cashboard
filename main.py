import streamlit as st

import investpy

# Obter lista de ações brasileiras
stocks = investpy.get_stocks_list(country='brazil')

# Ordenar a lista de tickets em ordem alfabética
sorted_stocks = sorted(stocks)

# Criar o combobox no Streamlit
selected_option = st.selectbox('Selecione uma opção', stocks)

# Exibir a opção selecionada
st.write('Você selecionou:', selected_option)
