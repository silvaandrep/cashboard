import streamlit as st
import pandas as pd
import investpy

# Obter lista de ações brasileiras
stocks = investpy.get_stocks_list(country='brazil')

# Criar um DataFrame pandas com os tickets das ações
df = pd.DataFrame({'Ticket': stocks})

st.table(df)
