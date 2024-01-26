from decimal import Decimal 

def pizza_order():
    '''Asking user for input about their order.'''
    print('''We offer: 
    1) Veggie Pizza.
    2) Pepperoni Pizza.
    3) Meat Pizza.
    4) Margherita Pizza.
    5) BBQ Chicken Pizza.
    6) Hawaiian Pizza.
    7) Buffalo Pizza.\n''')

    
    pizzas = {
    '1': 'Veggie Pizza',
    '2': 'Pepperoni Pizza',
    '3': 'Meat Pizza',
    '4': 'Margherita Pizza',
    '5': 'BBQ Chicken Pizza',
    '6': 'Hawaiian Pizza',
    '7': 'Buffalo Pizza'
    }

    while True:
        choice = input("Which pizza would you like (1-7)?: ")  
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            break
        print("Invalid choice, please try again")

    return pizzas[choice]

def no_of_pizzas(pizza):
    '''Asking for number of pizzas.'''
    while True:
        pizza_str = input(f"Enter the number of {pizza}: ") # Get input from user

        try:
            pizzas = int(pizza_str)
            if pizzas < 1:
                print("!!!ERROR!!! Please enter again\n")
                continue
            else:
                break

        except ValueError:
            print("!!!ERROR!!! Please enter a valid integer\n")
            continue

    return pizzas

def ask_delivery():
    '''Asking for delivery.'''
    while True:
        # Keep asking until valid input
        delivery = input("Is Delivery required? (y/n): ")
        delivery = delivery.lower()

        if (delivery == 'y') or (delivery == 'n'):
            break
        else:
            print(" !!!ERROR!!! Please enter only y or n.\n")
            continue

    return delivery

def ask_day():
    '''Asking what is the day today.'''
    while True:
        # Keep asking until valid input
        day = input("Is it Tuesday? (y/n): ")
        day = day.lower()

        if (day == 'y') or (day == 'n'):
            break
        else:
            print(" !!!ERROR!!! Please enter only y or n.\n")
            continue

    return day

def use_app():
    '''Asking whether user used BPP app.'''
    while True:
        # Keep asking until valid input
        app = input("Did the customer use app (y/n)?: ")
        app = app.lower()

        if (app == 'y') or (app == 'n'):
            break
        else:
            print(" !!!ERROR!!! Please enter only y or n.\n")
            continue

    return app

def calculate(pizza_number, deliver, today, application, price_of_all_pizza, delivery_cost = 2.5):
    '''Calculating the cost of pizza.'''

     # Conditions for calculating total price based on different scenarios
    
    if today == 'y' and deliver == 'y' and application == 'y' and pizza_number >= 5: # Apply 50% and 25% off
        total_price = Decimal((price_of_all_pizza - (50 / 100 * price_of_all_pizza))-(25 / 100 *price_of_all_pizza)) 

    elif today == 'n' and deliver == 'y' and application == 'y' and pizza_number >= 5: # Apply 25% off
        total_price = Decimal(price_of_all_pizza -(25 / 100 *price_of_all_pizza))  

    elif today == 'y' and deliver == 'y' and application == 'n' and pizza_number >= 5: # Apply 50% off
        total_price = Decimal(price_of_all_pizza - (50 / 100 * price_of_all_pizza)) 

    elif today == 'n' and deliver == 'y' and application == 'n' and pizza_number >= 5: # No discount
        total_price = Decimal(price_of_all_pizza )
  
    elif today == 'y' and deliver == 'y' and application == 'y': # Apply 50% and 25% off and added delivery cost
        total_price = Decimal(((price_of_all_pizza - (50 / 100 * price_of_all_pizza))-(25 / 100 *price_of_all_pizza)) + delivery_cost)

    elif today == 'n' and deliver == 'y' and application == 'y': # Apply 25% off and added delivery cost
        total_price = Decimal((price_of_all_pizza -(25 / 100 *price_of_all_pizza)) + delivery_cost)

    elif today == 'y' and deliver == 'n' and application == 'y': # Apply 50% and 25% off
        total_price = Decimal((price_of_all_pizza - (50 / 100 * price_of_all_pizza))-(25 / 100 *price_of_all_pizza))

    elif today == 'y' and deliver == 'y' and application == 'n': # Apply 50% off and added delivery cost
        total_price = Decimal((price_of_all_pizza - (50 / 100 * price_of_all_pizza)) + delivery_cost) 

    elif today == 'y' and deliver == 'n' and application == 'n': # Apply 50% off
        total_price = Decimal((price_of_all_pizza - (50 / 100 * price_of_all_pizza)))

    elif today == 'n' and deliver == 'y' and application == 'n': # Added delivery cost
        total_price = Decimal(price_of_all_pizza + delivery_cost)

    elif today == 'n' and deliver == 'n' and application == 'y': # Apply 25% off 
        total_price = Decimal(price_of_all_pizza-(25 / 100 *price_of_all_pizza))

    else: # No discount
        total_price = price_of_all_pizza

    return total_price



def display(total_cost, deliver, today, application, pizza_number, price_of_all_pizza, pizza, delivery_cost = 2.5):
    '''Print output.'''
    print("\n---------------------------------------BILL-------------------------------------\n")
    print("S.N  |Item Description\t\t |Price\t\t |Quantity\t\t | Total")
    print(f"1)   |{pizza}\t\t |£ 12\t\t |{pizza_number}\t\t\t |£ {price_of_all_pizza}\n")
    print("---------------------------------------------------------------------------------\n")
   
    if today == "y":
        print("Tuesday discount:\t\t\t\t\t\t\t  £",Decimal(50 / 100 * price_of_all_pizza))

    if application == "y" and today == "y":
        print("App order discount:\t\t\t\t\t\t\t  £",Decimal(((50 / 100 * price_of_all_pizza))-(25 / 100 *price_of_all_pizza)))

    if application == "y" and today != "y":
        print("App order discount:  \t\t\t\t\t\t\t  £",Decimal(25 / 100 *price_of_all_pizza))

    if deliver == "y" and pizza_number <= 5:
        print("Dilivery charge:  \t\t\t\t\t\t\t  £",delivery_cost)

    if deliver == "y" and pizza_number > 5:
        print("NO DELIVERY CHARGES.")

    print("\n---------------------------------------------------------------------------------")
    print("The total price of the pizza is:  \t\t\t\t\t  £",total_cost)
    print("\n\t\t\t\tTHANK YOU. PLEASE VISIT AGAIN. \n")

# Main part of the program
if __name__=="__main__":
    print("\n\t\t\t\t\t   WELCOME TO PIZZA HUB")
    print("\t\t\t\t\t=========================\n")
    pizza = pizza_order()
    pizza_number = no_of_pizzas(pizza)
    price = 12
    price_of_all_pizza = pizza_number * price
    today = ask_day()
    deliver = ask_delivery()
    application = use_app()
    total_cost = calculate(pizza_number, deliver, today, application, price_of_all_pizza)
    display(total_cost, deliver, today, application, pizza_number, price_of_all_pizza, pizza )

    
