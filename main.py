import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def get_exchange_rate(base_currency, target_currency):
    pair = f"{base_currency}{target_currency}=X"
    data = yf.Ticker(pair)
    hist = data.history(period="1d")

    if hist.empty:
        print(f"Failed to retrieve data for the currency pair {pair}.")
        return None

    return hist['Close'].iloc[0]

def display_top_currencies():
    top_currencies = {
        "USD": "United States Dollar",
        "EUR": "Euro",
        "JPY": "Japanese Yen",
        "GBP": "British Pound Sterling",
        "AUD": "Australian Dollar",
        "CAD": "Canadian Dollar",
        "CHF": "Swiss Franc",
        "CNY": "Chinese Yuan",
        "SEK": "Swedish Krona",
        "NZD": "New Zealand Dollar",
        "MXN": "Mexican Peso",
        "SGD": "Singapore Dollar",
        "HKD": "Hong Kong Dollar",
        "NOK": "Norwegian Krone",
        "KRW": "South Korean Won",
        "TRY": "Turkish Lira",
        "RUB": "Russian Ruble",
        "INR": "Indian Rupee",
        "BRL": "Brazilian Real",
        "ZAR": "South African Rand"
    }

    print("Top 20 strongest currencies in the world:")
    for code, name in top_currencies.items():
        print(f"{code}: {name}")


def convert_currency(amount, exchange_rate):
    return amount * exchange_rate


def main():
    base_currency = "USD"
    target_currency = "EUR"

    show_top_currencies = input(
        "Do you want to see a list of the top 20 strongest currencies in the world? (y/n): ").lower()
    if show_top_currencies == 'y':
        display_top_currencies()

    while True:
        user_base_currency = input(f"Enter the base currency code (default is {base_currency}): ").upper()
        user_target_currency = input(f"Enter the target currency code (default is {target_currency}): ").upper()
        base_currency = user_base_currency if user_base_currency else base_currency
        target_currency = user_target_currency if user_target_currency else target_currency

        try:
            amount = float(input(f"Enter the amount in {base_currency}: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue

        exchange_rate = get_exchange_rate(base_currency, target_currency)

        if exchange_rate is None:
            continue

        data_dir = Path('currency_data')
        data_dir.mkdir(exist_ok=True)

        pair = f"{base_currency}{target_currency}=X"
        data = yf.download(pair, start='2020-01-01', end='2023-01-01')

        csv_path = data_dir / 'exchange_rate_data.csv'
        data.to_csv(csv_path)

        df_exchange = pd.read_csv(csv_path, index_col=0)
        df_exchange.index = pd.to_datetime(df_exchange.index)

        plt.figure(figsize=(14, 7))
        plt.plot(df_exchange.index, df_exchange['Close'], label=f'{base_currency}/{target_currency} Exchange Rate')

        plt.xlabel('Date')
        plt.ylabel('Exchange Rate')
        plt.title(f'{base_currency}/{target_currency} Exchange Rate Over Time')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        plot_path = data_dir / 'exchange_rate_comparison.png'
        plt.savefig(plot_path)

        converted_amount = convert_currency(amount, exchange_rate)
        confirmation = input(
            f'Do you need a graphic of {base_currency}/{target_currency} exchange rate (y/n): ').lower()
        if confirmation == "y":
            print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
            plt.show()
        elif confirmation == "n":
            print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            print("Unexpected command")

if __name__ == "__main__":
    main()
