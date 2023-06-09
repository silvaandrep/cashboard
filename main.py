#import investpy
import streamlit as st

tickers = investpy.get_stocks_list(country='brazil')
tickers = sorted(tickers)

#st.sidebar.header('Menu de Ações da B3')

#ticker = st.sidebar.selectbox('Selecione uma ação: ', tickers)

#st.sidebar.write('Você selecionou ', ticker)

#st.header(ticker)
#st.write('Você selecionou ', ticker)
