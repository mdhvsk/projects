from Validators.integerValidator import validate_integer
from Validators.priceValidator import validate_price
from Validators.productCodeValidator import validate_product_code


def ask_update_values():
    print("Insert ID on next line")
    inventory_id = validate_integer()
    x = input("Product Code to be changed? Y or N: ")
    if x == "Y":
        product_code = validate_product_code()
    else:
        product_code = None

    y = input("Product Description to be changed? Y or N: ")
    if y == "Y":
        product_desc = input("Product Description: ")
    else:
        product_desc = None

    z = input("Price  to be changed? Y or N: ")
    if z == "Y":
        price = validate_price()
    else:
        price = None

    w = input("Quantity to be changed? Y or N: ")
    if w == "Y":
        quantity = validate_integer()
    else:
        quantity = None

    return inventory_id, product_code, product_desc, price, quantity
