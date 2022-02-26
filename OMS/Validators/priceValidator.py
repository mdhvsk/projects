def validate_price():
    while True:
        try:
            price = float(input("Price: "))
        except ValueError:
            print("Invalid Input, provide a price value of two decimal places")
            continue
        else:
            break
    return price