from Services.merchant import menu as merchant
from Services.customer import menu as customer
from mysqlConnector import MySQL


if __name__ == '__main__':
    mysql = MySQL.getInstance()
    mysql.open_connection()

    print("Welcome to the Market!\nAre You a Merchant or Customer? \n"+
          "Legend:\nM - Merchant\nC - Customer\nE - Exit")
    ans = input("Answer: ")
    while ans != 'E':
        if ans == 'M':
            print("\nWelcome Merchant!")
            merchant.display_home_menu()
        elif ans == 'C':
            print("\nWelcome Customer!")
            customer.displayHomeMenu()
        else:
            print("\nInvalid input, try again!")
        print("\nLegend:\nM - Merchant\nC - Customer\nE - Exit")
        ans = input("Answer: ")
    print("See you next time!")

    mysql.close_connection()

