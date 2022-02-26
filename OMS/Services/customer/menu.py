from Services.customer.list import showList
from Services.customer.order import placeOrder
def displayHomeMenu():
    print("Welcome Customer, would you like to see the list or place an order?")
    print("L - List\nP - Place Order\nH- Home")
    ans = input()
    while ans != "H":
        if ans == "L":
            list = showList()
            print(list)
        elif ans == "P":
            placeOrder()
        else:
            print("Invalid input, try again")
        print("L - List\nP - Place Order\nH- Home")
        ans = input()


