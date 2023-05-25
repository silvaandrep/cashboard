import streamlit as st
import pandas as pd
import investpy

# Obter lista de ações brasileiras
stocks = investpy.get_stocks_list(country='brazil')

# Criar um DataFrame pandas com os tickets das ações
df = pd.DataFrame({'Ticket': stocks})

# Exibir a tabela no Streamlit
def app():
    st.table(df)

# Executar o aplicativo Streamlit
if __name__ == '__main__':
    app()
