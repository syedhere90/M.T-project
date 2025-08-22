# Items available in Vegetable Store
veges = {
    1: {"Veg": "Potato", "price": 100.00},
    2: {"Veg": "Onion", "price": 80.00},
    3: {"Veg": "Tomato", "price": 50.00},
    4: {"Veg": "Cucumber", "price": 120.00},
    5: {"Veg": "Spinach", "price": 70.00},  # Fixed spelling
    6: {"Veg": "Ginger", "price": 50.00},
    7: {"Veg": "Brinjal", "price": 80.00},
    8: {"Veg": "Broccoli", "price": 40.00},
    9: {"Veg": "Radish", "price": 80.00},
    10: {"Veg": "Cauliflower", "price": 70.00},
}

# Function to calculate total and discount
def total_veg(cart):
    total = sum(veges[item]["price"] * qty for item, qty in cart.items())
    discount = 0
    if total >= 500:
        discount = total * 0.1  # 10% discount for orders over Rs 500
        total -= discount
    return total, discount

# Lambda function to calculate delivery days
deliv_days = lambda num_items: 3 if num_items <= 2 else 5

# Cart to store items and quantities
cart = {}

print("Welcome to My Vegy's Online Vegetable Store!")
print("\nAvailable Items:")
for key, value in veges.items():
    print(f"{key}. {value['Veg']} - Rs {value['price']:.2f}")

while True:
    print("\nMenu:")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Checkout")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item_num = input("Enter item number (1-10): ")
        if not item_num.isdigit() or int(item_num) not in veges:
            print("Error: Please enter a valid item number (1-10).")
            continue
        item_num = int(item_num)
        if item_num in cart:
            print(f"{veges[item_num]['Veg']} is already in cart. Updating quantity.")
        qty = input(f"Enter quantity for {veges[item_num]['Veg']} (e.g., 1, 2): ")
        if not qty.isdigit() or int(qty) <= 0:
            print("Error: Please enter a positive number for quantity.")
            continue
        cart[item_num] = cart.get(item_num, 0) + int(qty)
        print(f"Added {qty} x {veges[item_num]['Veg']} to cart.")

    elif choice == "2":
        if not cart:
            print("Cart is empty!")
            continue
        print("\nCart Contents:")
        for i, (item, qty) in enumerate(cart.items(), 1):
            print(f"{i}. {veges[item]['Veg']} - {qty} x Rs {veges[item]['price']:.2f} = Rs {qty * veges[item]['price']:.2f}")
        item_num = input("Enter item number to remove (or 'all' to clear cart): ")
        if item_num.lower() == "all":
            cart.clear()
            print("Cart cleared!")
            continue
        if not item_num.isdigit() or int(item_num) not in cart:
            print("Error: Invalid item number!")
            continue
        removed_item = int(item_num)
        qty = input(f"Enter quantity to remove for {veges[removed_item]['Veg']} (or 'all' to remove all): ")
        if qty.lower() == "all":
            del cart[removed_item]
            print(f"Removed all {veges[removed_item]['Veg']} from cart.")
        elif not qty.isdigit() or int(qty) <= 0:
            print("Error: Please enter a positive number for quantity.")
        else:
            qty = int(qty)
            if qty >= cart[removed_item]:
                del cart[removed_item]
                print(f"Removed all {veges[removed_item]['Veg']} from cart.")
            else:
                cart[removed_item] -= qty
                print(f"Removed {qty} x {veges[removed_item]['Veg']} from cart.")

    elif choice == "3":
        if not cart:
            print("Cart is empty!")
            continue
        print("\nCart Contents:")
        for i, (item, qty) in enumerate(cart.items(), 1):
            print(f"{i}. {veges[item]['Veg']} - {qty} x Rs {veges[item]['price']:.2f} = Rs {qty * veges[item]['price']:.2f}")

    elif choice == "4":
        break
    else:
        print("Error: Please enter 1, 2, 3, or 4!")

# Show checkout
if cart:
    print("\n--- Checkout ---")
    total, discount = total_veg(cart)
    for i, (item, qty) in enumerate(cart.items(), 1):
        print(f"Item {i}: {veges[item]['Veg']} - {qty} x Rs {veges[item]['price']:.2f} = Rs {qty * veges[item]['price']:.2f}")
    print(f"\nSubtotal: Rs {sum(veges[item]['price'] * qty for item, qty in cart.items()):.2f}")
    if discount > 0:
        print(f"Discount (10%): -Rs {discount:.2f}")
    print(f"Total: Rs {total:.2f}")
    print(f"Estimated delivery: {deliv_days(len(cart))} days")
else:
    print("\nCart is empty. Thanks for visiting!")