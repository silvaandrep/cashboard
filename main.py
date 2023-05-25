import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Definir o símbolo da ação desejada
symbol = 'AAPL'

# Obter os dados históricos da ação usando yfinance
stock = yf.Ticker(symbol)
data = stock.history(period="1y")

# Calcular a Média Móvel Simples (SMA)
sma_period = 50  # Período da SMA
data['SMA'] = data['Close'].rolling(window=sma_period).mean()

# Calcular o Índice de Força Relativa (RSI)
rsi_period = 14  # Período do RSI
delta = data['Close'].diff()
gain = delta.mask(delta < 0, 0)
loss = -delta.mask(delta > 0, 0)
avg_gain = gain.rolling(window=rsi_period).mean()
avg_loss = loss.rolling(window=rsi_period).mean()
rs = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))
data['RSI'] = rsi

# Exibir tabela com os indicadores
st.write(data[['Close', 'SMA', 'RSI']])

# Gráfico com os indicadores
fig, ax = plt.subplots()
ax.plot(data.index, data['Close'], label='Preço')
ax.plot(data.index, data['SMA'], label='SMA')
ax.legend()
ax.set_title(f'Indicadores para {symbol}')
ax.set_xlabel('Data')
ax.set_ylabel('Valor')

# Exibir o gráfico no Streamlit
st.pyplot(fig)
