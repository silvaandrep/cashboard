import investpy
import yfinance as yf
import plotly.graph_objects as go
import streamlit as st

# Obter lista de ações brasileiras
stocks = investpy.get_stocks_list(country='brazil')

# Ordenar a lista de tickets em ordem alfabética
sorted_stocks = sorted(stocks)


# Criar o combobox no Streamlit
#selected_option = st.selectbox('Selecione uma opção', stocks)

# Exibir a opção selecionada
#st.write('Você selecionou:', selected_option)

# Configurar o título do aplicativo
st.title('Gráfico de Velas - PETR3.SA')


# Configurar a barra lateral
st.sidebar.header('Coluna 1')


#valor = st.sidebar.slider('Selecione um valor', 0, 100, 50)
opcao = st.sidebar.selectbox('Selecione uma ação', stocks)
st.sidebar.write('Você selecionou ', opcao)

# Adicionar elementos à coluna principal
st.header('Coluna 2')
st.write(opcao)

opcao = opcao + ".SA"

# Obter os dados da ação PETR3.SA usando a biblioteca yfinance
data = yf.download(opcao, start='2022-01-01', end='2022-12-31')

# Criar o gráfico de velas usando o Plotly
fig = go.Figure(data=[go.Candlestick(x=data.index,
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'])])

# Configurar o layout do gráfico
fig.update_layout(xaxis_rangeslider_visible=False)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)
