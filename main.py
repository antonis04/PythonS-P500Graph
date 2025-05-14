import yfinance as yf
import matplotlib.pyplot as plt

# Pobierz Dane S&P 500 za kwiecień 2025
sp500 = yf.download('^GSPC', start='2025-04-01', end='2025-05-01')

# Początkowa kwota inwestycji
initial_investment = 100000

# Oblicz wartość portfela na podstawie ceny zamknięcia (Close)
sp500['Portfolio Value'] = (sp500['Close'] / sp500['Close'].iloc[0]) * initial_investment

# Wykres
plt.figure(figsize=(10,6))
plt.plot(sp500.index, sp500['Portfolio Value'], label='S&P 500')
plt.title('Symulacja inwestycji 100 000 USD w indeks S&P 500 (kwiecień 2025)')
plt.xlabel('Data')
plt.ylabel('Wartość portfela [USD]')
plt.legend()
plt.grid(True)
plt.show()
