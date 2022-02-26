from Validators.productCodeValidator import validate_product_code
from Validators.priceValidator import validate_price
from Validators.integerValidator import validate_integer


def ask_add_values():
    product_code = validate_product_code()
    product_desc = input("Product Desc: ")
    price = validate_price()
    print("Quantity in next line")
    quantity = validate_integer()

    return product_code, product_desc, price, quantity



