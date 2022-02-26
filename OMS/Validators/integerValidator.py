def validate_integer():
    while True:
        try:
            integer = int(input("Integer Value: "))
        except ValueError:
            print("Input an integer value")
            continue
        if integer < 0:
            print("Integer must be greater than 0")
            continue
        else:
            break
    return integer

