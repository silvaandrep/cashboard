import streamlit as st

# Lista de opções para o combobox
opcoes = ['Opção 1', 'Opção 2', 'Opção 3']

#st.title('Título página')

st.sidebar.header('Header Sidebar')
st.sidebar.write('Write Sidebar')

# Criar o combobox no Streamlit
selected_option2 = st.sidebar.selectbox('Selecione uma ação', stocks)

# Exibir a opção selecionada
st.sidebar.write('Você selecionou ', selected_option2)

st.header('Header Principal')
st.write('Você selecionou')

# Criar o combobox no Streamlit
selected_option = st.selectbox('Selecione uma opção', opcoes)

# Exibir a opção selecionada
st.write('Você selecionou:', selected_option)

