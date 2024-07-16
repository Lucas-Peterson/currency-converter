import yfinance as yf


def get_exchange_rate(base_currency, target_currency):
    pair = f"{base_currency}{target_currency}=X"
    data = yf.Ticker(pair)
    hist = data.history(period="1d")

    if hist.empty:
        print("Failed to retrieve data for the currency pair.")
        return None

    return hist['Close'].iloc[0]


def convert_currency(amount, exchange_rate):
    return amount * exchange_rate


def main():
    base_currency = input("Enter the base currency code (e.g., USD): ")
    target_currency = input("Enter the target currency code (e.g., EUR): ")
    amount = float(input(f"Enter the amount in {base_currency}: "))

    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Failed to retrieve the exchange rate.")


if __name__ == "__main__":
    main()
