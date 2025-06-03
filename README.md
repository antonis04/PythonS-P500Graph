# S&P 500 Investment Simulation

This project simulates an investment in the S&P 500 index for the month of April 2025. It was created as part of a bachelor's thesis to demonstrate how the value of a portfolio changes over time when tracking a major stock market index.

## Features
- Downloads historical S&P 500 data for April 2025 using the `yfinance` library.
- Simulates an initial investment of $100,000.
- Calculates the portfolio value over time based on the closing prices.
- Visualizes the investment growth with a clear and informative matplotlib chart.

## How It Works
1. The script fetches daily S&P 500 data for the specified period.
2. It calculates how the value of a $100,000 investment would change, assuming the investment was made at the start of April 2025 and held throughout the month.
3. The results are plotted, showing the portfolio value for each trading day.

## Requirements
- Python 3.x
- [yfinance](https://pypi.org/project/yfinance/)
- [matplotlib](https://matplotlib.org/)

You can install the required libraries using pip:

```bash
pip install yfinance matplotlib
```

## Usage
Run the script with Python:

```bash
python main.py
```

A chart will appear, showing the simulated portfolio value over time.

## Purpose
This program was developed for academic purposes, specifically for a bachelor's thesis, to illustrate the dynamics of passive investment in a major stock index over a short period.

