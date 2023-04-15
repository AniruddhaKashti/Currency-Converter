# Define exchange rates
AUDUSD = 0.8371
CADUSD = 0.8711
USDCNY = 6.1715
EURUSD = 1.2315
GBPUSD = 1.5683
NZDUSD = 0.7750
USDJPY = 119.95
EURCZK = 27.6028
EURDKK = 7.4405
EURNOK = 8.6651

# Prompt user for input
from_currency = input("Enter the currency code you want to convert from: ")
to_currency = input("Enter the currency code you want to convert to: ")
amount = float(input("Enter the amount you want to convert: "))

# Define conversion function
def convert_currency(from_curr, to_curr, amount):
    if from_curr == "AUD" and to_curr == "USD":
        return amount * AUDUSD
    elif from_curr == "CAD" and to_curr == "USD":
        return amount * CADUSD
    elif from_curr == "USD" and to_curr == "CNY":
        return amount * USDCNY
    elif from_curr == "EUR" and to_curr == "USD":
        return amount * EURUSD
    elif from_curr == "GBP" and to_curr == "USD":
        return amount * GBPUSD
    elif from_curr == "NZD" and to_curr == "USD":
        return amount * NZDUSD
    elif from_curr == "USD" and to_curr == "JPY":
        return amount * USDJPY
    elif from_curr == "EUR" and to_curr == "CZK":
        return amount * EURCZK
    elif from_curr == "EUR" and to_curr == "DKK":
        return amount * EURDKK
    elif from_curr == "EUR" and to_curr == "NOK":
        return amount * EURNOK
    else:
        return None

# Call conversion function and print result
result = convert_currency(from_currency.upper(), to_currency.upper(), amount)

if result is not None:
    print(f"{from_currency} {amount:.2f} = {to_currency} {result:.2f}")
else:
    print(f"Unable to find rate for {from_currency}/{to_currency}")
