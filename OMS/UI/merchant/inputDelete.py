from Validators.integerValidator import validate_integer


def ask_delete_values():
    print("Input ID on next line")
    inventory_id = validate_integer()

    return inventory_id
