Items = {
    "Drinks": {
        "Coke": 4,
        "Pepsi": 4,
        "Sprite": 3,
        "Water": 3,
        "Apple Juice": 3,
    },
    "Snacks": {
        "Chips": 5,
        "Popcorn": 5,
        "Salted Nuts": 3,
        "Chocolate": 6,
        "Candy": 3,
    },
    "Alcohol": {
        "Vodka": 40,
        'Beer': 15,
        'Whiskey': 30,
    },
    "Ready to Eat Meals": {
        "Hotdog": 10,
        "Pizza": 18,
        "Burger": 13
    }
}

cart = [
    ''
]

print("Welcome to the shop!\n")

# Display items and prices
output_string = ""
for category, items in Items.items():
    output_string += f"{category}:\n"
    for item, price in items.items():
        output_string += f"  {item}: {price} PLN\n"

print(output_string)

def Main():
    total_owed = 0
    cart = []  
    while True:
        userSelectedItem = input("What would you like? (type in lowercase, type 'done' to exit, type 'cart' to see your cart): ").strip()
        if userSelectedItem == "cart".lower():
            print("Cart: ")
            for item, quantity in cart:
                print(f"{item}")
            else:
                print("Cart is empty.")
                continue
        if userSelectedItem == "done":
            break
        elif userSelectedItem == 'coke'.lower():
            total_owed += Items["Drinks"]["Coke"]
            print("You added a Coke to your cart.")
            continue
        elif userSelectedItem == 'pepsi'.lower():
            total_owed += Items["Drinks"]["Pepsi"]
            print("You added a Pepsi to your cart.")
            continue
        elif userSelectedItem =='sprite'.lower():
            total_owed += Items["Drinks"]["Sprite"]
            print("You added a Sprite to your cart.")
            continue
        elif userSelectedItem == 'water'.lower():
            total_owed += Items["Drinks"]["Water"]
            print("You added Water to your cart.")
            continue
        elif userSelectedItem == 'apple juice'.lower() or userSelectedItem == 'juice'.lower():
            total_owed += Items["Drinks"]["Apple Juice"]
            print("You added an Apple Juice to your cart.")
            continue
        elif userSelectedItem == 'chips'.lower():
            total_owed += Items["Snacks"]["Chips"]
            print("You added Chips to your cart.")
            continue
        elif userSelectedItem == 'popcorn'.lower():
            total_owed += Items["Snacks"]["Popcorn"]
            print("You added Popcorn to your cart.")
            continue
        elif userSelectedItem =='salted nuts'.lower() or userSelectedItem == 'nuts'.lower():
            total_owed += Items["Snacks"]["Salted Nuts"]
            print("You added Salted Nuts to your cart.")
            continue
        elif userSelectedItem == 'chocolate'.lower():
            total_owed += Items["Snacks"]["Chocolate"]
            print("You added Chocolate to your cart.")
            continue
        elif userSelectedItem == 'candy'.lower():
            total_owed += Items["Snacks"]["Candy"]
            print("You added Candy to your cart.")
            continue
        elif userSelectedItem == 'vodka'.lower():
            alcohol1 = input("You must be 18 or more to buy alcohol. Are you 18+? (y/n)").lower()
            if alcohol1 == 'y':
                
            
                total_owed += Items["Snacks"]["Candy"]
                print("You added Vodka to your cart.")
                continue
            elif alcohol1 == 'n':
                print("You are not 18+. You cannot purchase alcohol.")
                continue

        found_item = False
        for category, items in Items.items():
            if userSelectedItem in items:
                found_item = True
                price = Items[category][userSelectedItem]
                quantity = 1  
                cart.append((userSelectedItem, quantity))
                print(f"You added a {userSelectedItem} to your cart.")
                break

        if not found_item:
            print("Invalid item. Please try again.")

    print("\nYour cart:")
    for item, quantity in cart:
        print(f"  {item}: {quantity}")

    print(f"\nTotal amount owed: {total_owed:.2f} PLN")

if __name__ == "__main__":
    Main()
