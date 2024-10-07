# Currency Exchange Rate Converter

This project provides a simple command-line tool that allows users to check the exchange rate between two currencies, convert amounts between them, and visualize historical exchange rate trends. The program fetches data from Yahoo Finance using the `yfinance` Python library.

## Features

- Retrieve the exchange rate between two currencies.
- Convert a specified amount from the base currency to the target currency.
- Display a list of the top 20 strongest currencies in the world.
- Download historical exchange rate data (from 2020 to 2023).
- Visualize exchange rate trends in a plot, saved as an image.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Required Python packages:
  - `yfinance`
  - `pandas`
  - `matplotlib`
  - `pathlib`

You can install the required libraries with the following command:

```bash
pip install yfinance pandas matplotlib
