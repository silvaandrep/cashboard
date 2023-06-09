import investpy
import streamlit as st

tickers = investpy.get_stocks_list(country='brazil')

tickers = sorted(tickers)

selected_option = st.selectbox('Selecione uma opção', stocks)
