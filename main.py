import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

sp500 = yf.download('^GSPC', start='2025-04-01', end='2025-05-01')

initial_investment = 100000
sp500['Portfolio Value'] = (sp500['Close'] / sp500['Close'].iloc[0]) * initial_investment

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(16, 9))

ax.plot(sp500.index, sp500['Portfolio Value'], label='Wartość portfela S&P 500', marker='o', linestyle='-',
        color='dodgerblue', linewidth=2, markersize=6)
ax.fill_between(sp500.index, sp500['Portfolio Value'], alpha=0.15, color='dodgerblue')

ax.set_title('Symulacja inwestycji 100 000 USD w indeks S&P 500 (Kwiecień 2025)', fontsize=20, fontweight='bold', pad=25)
ax.set_xlabel('Data', fontsize=15, labelpad=18)
ax.set_ylabel('Wartość portfela [USD]', fontsize=15, labelpad=18)

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=4))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right", fontsize=11)
plt.setp(ax.get_yticklabels(), fontsize=11)

ax.legend(fontsize=13, loc='upper left', frameon=True, framealpha=0.9)

ax.grid(True, linestyle='--', alpha=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('gray')
ax.spines['bottom'].set_color('gray')

final_value = sp500['Portfolio Value'].iloc[-1]
return_rate = ((final_value - initial_investment) / initial_investment) * 100
return_text = f"Stopa zwrotu w kwietniu 2025: {return_rate:.2f}%"
final_value_text = f"Końcowa wartość portfela: {final_value:,.2f} USD"

last_date = sp500.index[-1]
vertical_offset = (ax.get_ylim()[1] - ax.get_ylim()[0]) * 0.015
ax.text(last_date, final_value + vertical_offset,
        f'{final_value:,.2f} USD',
        fontsize=12, color='darkgreen', ha='center', va='bottom',
        bbox=dict(boxstyle="round,pad=0.4", fc="ivory", ec="gray", lw=0.7, alpha=0.85))

fig.text(0.5, 0.060, final_value_text, ha='center', va='bottom', fontsize=14, color='black', fontweight='bold')
fig.text(0.5, 0.030, return_text, ha='center', va='bottom', fontsize=14, color='black')
fig.text(0.5, 0.005, 'Dane pobrane przy użyciu biblioteki yfinance.', ha='center', va='bottom', fontsize=10, color='dimgray')

plt.tight_layout(rect=(0.03, 0.08, 0.97, 0.94))

plt.show()
