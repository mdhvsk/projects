def validate_product_code():
    while True:
        try:
            product_code = input("Product Code: ")
            if len(product_code) == 3:
                break
        except AssertionError:
            print("Code must be 3 Letters Long")
    return product_code