import streamlit as st
import investpy

# Obter lista de ações brasileiras
stocks = investpy.get_stocks_list(country='brazil')

# Ordenar a lista de tickets em ordem alfabética
sorted_stocks = sorted(stocks)

# Dividir a tela em 1/3 e 2/3
col1, col2 = st.columns([1, 2])

# Adicionar elementos à primeira coluna
with col1:
    st.header('Coluna 1')
    st.write('Conteúdo da coluna 1')
    
# Criar o combobox no Streamlit
selected_option = st.selectbox('Selecione uma opção', stocks)

# Exibir a opção selecionada
st.write('Você selecionou:', selected_option)

# Adicionar elementos à segunda coluna
with col2:
    st.header('Coluna 2')
    st.write('Conteúdo da coluna 2')
