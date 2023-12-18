def display(cart):
    total = 0
    print("\t\t Receipt")
    if not cart:
        print("You have no items in your cart")
    else:
        for name, value in cart.items():
            print((f"\t{name} - ${value["price"]:.2f} x {value["quantity"]}"))
            total += value["price"] * value["quantity"]
    print(f"total: ${total:.2f}")
    
def cart_add(cart):
    name = input('Enter the item you wish to buy: ').title()
    if name in cart:
        quantity = int(input(f"How Many more {name}s would you like to add? "))
        cart[name]['quantity'] += quantity
    else:
        price = float(input(f"What is the price of the {name}? "))
        quantity = int(input(f"How many {name}s do you want? "))
        cart[name] = {"price": price, "quantity": quantity}

def cart_remove(cart):
    display(cart)
    name = input("What would you like to remove? ").title()
    if name not in cart:
        print(f"You don't have any {name}s")
    else:
        quantity = int(input(f"How many {name}s would you like to remove? "))
        cart[name]["quantity"] -= quantity
        if cart[name]["quantity"] <= 0:
            del cart[name]
    display(cart)

def cart_delete(cart):
    answer = input("Would you like to entirely delete your cart? Yes or No: ").lower()
    while answer not in ["yes", "no"]:
        answer = input("Incorrect Response. Please enter only yes or no").lower()
    if answer == "yes":
        cart.clear()
        print("Your cart has been emptied entirely")

def shopping_cart():
    print("Welcome to McSpanky's! What can I get ya?")
    # Create an empty dictionary
    cart = {}
    # Start a loop that will continue to run until the user quit
    while True:
        # Ask what the user would like to do
        answer = input('What would you like to do? Add/Remove/Show/Clear/Quit ').lower()
        while answer not in ["add","remove","show","clear","quit"]:
            answer = input("Incorrect Response. Please enter only Add/Remove/Show/Clear/Quit ").lower()
        # If the user enters 'quit', stop the loop
        if answer == 'quit':
            break
        # If the user enters 'add'
        elif answer == 'add':
            cart_add(cart)
            display(cart)
        # If the user enters 'remove'
        elif answer == 'remove':
            cart_remove(cart)
        elif answer == 'show':
            display(cart)
        elif answer == 'clear':
            cart_delete(cart)
        else:
            break
    # Once the user quits, print the cart receipt
    print("Thanks for shopping wiht us. Here's your receipt!")
    display(cart)
    
    
    
shopping_cart()