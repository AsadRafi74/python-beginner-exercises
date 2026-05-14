def check_rates():
    currency = input ("enter currency:")
    # from_currency = input("from currency:")
    to_currency  = input("to currency :")
    amount = float(input("enter your amount :"))
    rates = {
        "usd" :1,
        "dinar" : 970,
        "rial" : 72,
        "yuan" : 12,
        "pkr" : 270
         
    }
    converted = amount * rates[currency]
    print(converted)

check_rates()
    