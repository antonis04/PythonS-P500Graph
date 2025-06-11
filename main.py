import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

sp500 = yf.download('^GSPC', start='2025-04-01', end='2025-05-01')

initial_investment = 100000

sp500['Portfolio Value'] = (sp500['Close'] / sp500['Close'].iloc[0]) * initial_investment

plt.style.use('seaborn-v0_8-darkgrid')
plt.figure(figsize=(12, 7))

plt.plot(sp500.index, sp500['Portfolio Value'], label='Wartość portfela S&P 500', marker='o', linestyle='-',
         color='skyblue')
plt.fill_between(sp500.index, sp500['Portfolio Value'], alpha=0.1, color='skyblue')

plt.title('Symulacja inwestycji 100 000 USD w indeks S&P 500 (Kwiecień 2025)', fontsize=16)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Wartość portfela [USD]', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.gcf().autofmt_xdate()

final_value = sp500['Portfolio Value'].iloc[-1]
return_rate = ((final_value - initial_investment) / initial_investment) * 100
return_text = f"Stopa zwrotu w kwietniu 2025: {return_rate:.2f}%"

plt.figtext(0.5, 0.01, 'Dane pobrane przy użyciu biblioteki yfinance.', ha='center', va='bottom', fontsize=10,
            color='gray')
plt.figtext(0.5, 0.05, return_text, ha='center', va='bottom', fontsize=12, color='black')

plt.show()
