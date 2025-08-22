# Shopping cart
items = {
    1: {"name": "Book", "price": 9.99},
    2: {"name": "Headphones", "price": 29.99},
    3: {"name": "T-Shirt", "price": 14.99}
}

# Function to calculate total with shipping
def calculate_total(cart):
    total = sum(items[item]["price"] for item in cart)
    if total < 50:
        shipping = 5.00
        total += shipping
        print(f"Shipping fee added: ${shipping:.2f}")
    return total

# Lambda to estimate delivery days
delivery_days = lambda num_items: 3 if num_items <= 2 else 5

# Cart to store items
cart = []

# Main loop
print("Welcome to Grok's Online Store!")
print("Items:")
for key, value in items.items():
    print(f"{key}. {value['name']} - ${value['price']:.2f}")

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Checkout")
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        item_num = input("Enter item number (1-3): ")
        if not item_num.isdigit() or int(item_num) not in items:
            print("Invalid item number!")
            continue
        cart.append(int(item_num))
        print(f"Added {items[int(item_num)]['name']} to cart.")
    
    elif choice == "2":
        if not cart:
            print("Cart is empty!")
            continue
        print("Cart:")
        for i, item in enumerate(cart, 1):
            print(f"{i}. {items[item]['name']}")
        item_num = input("Enter item number to remove: ")
        if not item_num.isdigit() or not 1 <= int(item_num) <= len(cart):
            print("Invalid item number!")
            continue
        removed_item = cart.pop(int(item_num)-1)
        print(f"Removed {items[removed_item]['name']} from cart.")
    
    elif choice == "3":
        break
    else:
        print("Please enter 1, 2, or 3!")

# Show checkout
if cart:
    print(f"\n--- Checkout ---")
    for i, item in enumerate(cart, 1):
        print(f"Item {i}: {items[item]['name']} - ${items[item]['price']:.2f}")
    total = calculate_total(cart)
    print(f"Total: ${total:.2f}")
    print(f"Estimated delivery: {delivery_days(len(cart))} days")
else:
    print("\nCart is empty. Thanks for visiting!")