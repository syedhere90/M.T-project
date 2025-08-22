# Define the menu as a dictionary with items and prices
menu = {
    1: {"item": "Burger", "price": 8.99},
    2: {"item": "Pizza", "price": 12.99},
    3: {"item": "Salad", "price": 6.99},
    4: {"item": "Soda", "price": 2.99}
}

# Define a function to calculate total cost with a discount for large orders
def calculate_total(order):
    total = sum(menu[item]["price"] for item in order)
    if total > 20:
        discount = total * 0.1  # 10% discount for orders over $20
        total -= discount
        print(f"Applied a 10% discount! Saved ${discount:.2f}")
    return total

# Lambda function to estimate preparation time based on number of items
prep_time = lambda num_items: 5 + num_items * 2  # 5 minutes base + 2 minutes per item

# List to store the user's order
order = []

# Welcome message
print("Welcome to Grok's Diner!")
print("Menu:")
for key, value in menu.items():
    print(f"{key}. {value['item']} - ${value['price']:.2f}")

# Main ordering loop using while
while True:
    # Get user input
    user_input = input("\nEnter the menu number to order (or 'done' to finish): ")
    
    # Check if user wants to finish
    if user_input.lower() == 'done':
        break
    
    # Check if input is a valid number
    if not user_input.isdigit():
        print("Please enter a valid number or 'done'!")
        continue
    
    # Convert input to integer and validate
    choice = int(user_input)
    if choice not in menu:
        print("Invalid menu item! Please choose a number from the menu.")
        continue
    
    # Add valid choice to order
    order.append(choice)
    print(f"Added {menu[choice]['item']} to your order.")

# Process the order if it's not empty
if order:
    print("\n--- Order Summary ---")
    # Use for loop to display ordered items
    for i, item in enumerate(order, 1):
        print(f"Item {i}: {menu[item]['item']} - ${menu[item]['price']:.2f}")
    
    # Calculate and display total using def function
    total_cost = calculate_total(order)
    print(f"Total cost: ${total_cost:.2f}")
    
    # Use lambda function to estimate preparation time
    time = prep_time(len(order))
    print(f"Estimated preparation time: {time} minutes")
    
    print("\nThank you for dining at Grok's Diner! Your order is being prepared.")
else:
    print("\nNo items ordered. Goodbye!")

