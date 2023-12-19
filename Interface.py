from typing import Any
from Products import *
import time
class Interface:   

    def main_page(order):
        order_aux = order
        print("1. See all the clothes")
        print("2. My order")
        print("3. Pay")
        option = int(input("Enter an option between 1 and 3: "))
        print("\n")
        if option ==1 :
            order_aux=Interface.see_products(order)
        elif option == 2:
            Interface.my_order(order_aux)
        elif option == 3:
            Interface.pay(order)
        else:
            print("invalid input")
            Interface.main_page(order)
    def see_products(order):
        option = -1
        prod = SavingProcess.verify_if_json_exists()
        for i in range (0, len(prod)):
            print(f"{i+1}. {prod[i].get_description()}")
        option = input("Choose the index number of the product or if you want to go to main page write 'exit': ")
        if option.lower() == 'exit':
            print("Exiting to the main page.")
            Interface.main_page(order)
            return order
        else:
            ok = 0
            try:
                index = int(option)
                if 1 <= index <= len(prod):
                    print(f"You selected product at index {index}.")
                    
                    order.append(prod[index-1])
                    SavingProcess.remove_element(index)
                    ok =1
                    Interface.see_products(order)
                else:
                    print("Index out of range. Please enter a valid index.")
            except ValueError:
                print("Invalid input. Please enter a valid index or 'exit'.")
            if ok != 1:
                Interface.see_products(order)
                print("Invalid input. Please enter a valid index or 'exit'.")
    def my_order(order):
        n = 0
        total = 0
        for x in order:
            n = n + 1
            total = total + x.price
            print(f"{n}. {x.get_description()}")
        print(f"Your total is {total}$")
        option = int (input("1. Back to main page\n2. Procced to pay\nEnter option: "))
        if(option == 1):
            Interface.main_page(order)
        elif(option == 2):
            Interface.pay(order)
        else:
            print("Press 1 or 2\n\n")
            time.sleep(1.5)
            Interface.my_order(order)
    def pay(order):
        total = 0
        n = 0
        if len(order) != 0:
            print("Are you sure you want to buy:")
        for x in order:
            n = n+1
            print(f"{n}. {x.get_description()}")
            total = total + x.price
        if total != 0:
            print(f"Total: {total}$")
            option = int(input("\n1. Yes\n2. No\nPress 1 or 2: "))
            if option == 1: 
                print(f"Thank you for your purchase!")
                order.clear()
                time.sleep(2)
                Interface.main_page(order)
            elif option ==2: 
                Interface.main_page(order)    
            else:
                print("Invalid option")
                Interface.pay(order)
        else:
            print("You did not select anything\nYou will be redirected to the main page\n")
            time.sleep(2)
            Interface.main_page(order)

    