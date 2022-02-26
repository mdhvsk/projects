from Services.merchant.add import callAdd
from Services.merchant.update import callUpdate
from Services.merchant.delete import callDelete
from Services.merchant.list import callList
from UI.merchant.inputAdd import ask_add_values
from UI.merchant.inputDelete import ask_delete_values
from UI.merchant.inputUpdate import ask_update_values

def display_home_menu():
    print("Welcome Merchant, what would you like to do? \nA - Add\n"
          "U - Update\nD - Delete\nL - List\nH - Home")
    ans = input()
    while ans != 'H':
        if ans == "A":  #Add
            product_code, product_desc, price, quantity = ask_add_values()
            callAdd(product_code, product_desc, price, quantity)
        elif ans == "U":    #Update
            print(callList())
            inventory_id, product_code, product_desc, price, quantity = ask_update_values()
            callUpdate(inventory_id, product_code, product_desc, price, quantity)
        elif ans == "D":    #Delete
            print(callList())
            inventory_id = ask_delete_values()
            callDelete(inventory_id)
        elif ans == "L":    #List
            merchant_list = callList()
            print(merchant_list)
        else:
            print("Input Error, Try Again")
        print("A - Add\nU - Update\nD - Delete\nL - List\nH - Home")
        ans = input()



