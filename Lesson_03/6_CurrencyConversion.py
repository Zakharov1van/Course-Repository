currency_code = input("Enter the code of your currency (UAH/USD/EUR): ").lower()
if currency_code != "uah" and currency_code != "usd" and currency_code != "eur":
    print("You entered wrong currency code!")
else:
    amount = float(input("Enter the amount of money: "))
    wanted_currency_code = input("Enter the code of the currency that you want to convert to (UAH/USD/EUR): ").lower()
    if wanted_currency_code != "uah" and wanted_currency_code != "usd" and wanted_currency_code != "eur":
        print("You can convert money only in UAH, USD or EUR")
    else:
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
