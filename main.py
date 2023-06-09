import investpy as ip
import streamlit as st

opcoes = ['Opção 1', 'Opção 2', 'Opção 3']

# Criar o combobox no Streamlit
selected_option = st.selectbox('Selecione uma opção', opcoes)

st.title('Title Principal')
st.header('Header Principal')
st.write('Você selecionou:', selected_option)
st.sidebar.header('Header Sidebar')
st.sidebar.write('Write Sidebar')

