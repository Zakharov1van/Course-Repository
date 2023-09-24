currency_code = input("Enter the code of your currency (UAH/USD/EUR): ").lower()
amount = float(input("Enter the amount of money: "))
wanted_currency_code = input("Enter the code of the currency that you want to convert to (UAH/USD/EUR): ").lower()
if currency_code == "uah":
    if wanted_currency_code == "usd":
        converted = amount / 36.5686
    else:
        converted = amount / 38.8944
elif currency_code == "usd":
    converted = amount * 36.5686
else:
    converted = amount * 38.8944

print(f"Result is {converted}")
