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
        elif user_input == "3":
            buying_price = int(input("buying price: "))
            rent = int(input("rent: "))
            return_yield = buy_and_rent_yield(buying_price, rent)
            print(f"return {return_yield}%")
        elif user_input == "4":
            hon_azmi = int(input("hon azmi: "))
            mashcanta = int(input("mashcanta: "))
            ribit = float(input("ribit: "))
            rent = int(input("rent: "))
            return_yield = minuf_yield(hon_azmi, mashcanta, ribit, rent)
            print(f"return {return_yield}%")
        elif user_input == "5":
            rent = int(input("rent: "))
            hivun_rate = float(input("hivun rate: "))
            price = hivun(rent, hivun_rate)
            print(f"price: {price}")
        elif user_input == 'q':
            print("good bye")
        else:
            print("unkwown command")

def menu():
    print("======================================================")
    print("[1] buy property in Y money and make X money in a year")
    print("[2] buy and sell in X months")
    print("[3] buy and rent")
    print("------------------------------------------------------")
    print("[4] return with minuf")
    print("------------------------------------------------------")
    print("[5] hivun")
    print("------------------------------------------------------")
    print("[q] exit")
    print("======================================================")
    
main()