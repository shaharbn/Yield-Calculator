from property import *

def main():
    properties = []
    user_input = "starting"
    while user_input != "q":
        menu()
        user_input = input()
        if user_input == "1":
            buying_price = int(input("Enter your buying price: "))
            properties.append(Property())
        elif user_input == 'q':
            print("good bye")

def menu():
    print("[1] add a property")
    print("[q] exit")
    
main()

