import investpy
import yfinance as yf
import plotly.graph_objects as go
import streamlit as st

tickers = investpy.get_stocks_list(country='brazil')
tickers = sorted(tickers)

st.sidebar.header('MENU DE AÇÕES DA B3')

ticker = st.sidebar.selectbox('Selecione uma ação: ', tickers)

ticker = ticker + ".SA"

st.sidebar.write('Total de ações da B3: ', len(tickers))


st.header(ticker)
st.write('Você selecionou ', ticker)

períodos = ['5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'max']

periodo = st.sidebar.selectbox('Selecione o período: ', períodos)

dados = yf.download(ticker, period=periodo)

fig = go.Figure(data=go.Scatter(x=dados.index, y=dados['Close']))
fig.update_layout(title=f"Gráfico de Preço de Fechamento para {ticker}")
st.plotly_chart(fig)
