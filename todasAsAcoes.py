import investpy

# Obter lista de ações brasileiras
stocks = investpy.get_stocks_list(country='brazil')

# Ordenar a lista de tickets em ordem alfabética
sorted_stocks = sorted(stocks)

# Imprimir os tickets das ações brasileiras em ordem alfabética
for stock in sorted_stocks:
    print(stock)
