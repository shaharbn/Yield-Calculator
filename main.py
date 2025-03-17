from formulas import *

def main():
    print("האושת ןובשחמ")
    user_input = "starting"
    while user_input != "q":
        menu()
        user_input = input()
        if user_input == "1":
            buying_price = int(input("buying price: "))
            x_per_year = int(input("how much you make per year: "))
            return_yield = buy_and_make_by_year_yield(buying_price, x_per_year)
            print(f"return {return_yield}%")
        elif user_input == "2":
            buying_price = int(input("buying price: "))
            selling_price = int(input("selling price: "))
            months = int(input("months: "))
            return_yield = buy_and_sell_in_x_month(buying_price, selling_price, months)
            print(f"return {return_yield}%")
        elif user_input == 'q':
            print("good bye")

def menu():
    print("[1] buy property in Y money and make X money in a year")
    print("[2] buy and sell in X months")
    print("[q] exit")
    
main()