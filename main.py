import streamlit as st

st.title('Título página')
st.header('Header Principal')
st.write('Você selecionou')
st.sidebar.header('Header Sidebar')
st.sidebar.write('Write Sidebar')

# Lista de opções para o combobox
opcoes = ['Opção 1', 'Opção 2', 'Opção 3']

# Criar o combobox no Streamlit
selected_option = st.selectbox('Selecione uma opção', opcoes)

# Exibir a opção selecionada
st.write('Você selecionou:', selected_option)
