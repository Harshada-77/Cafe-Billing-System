# Cafe Billing System
# Menu
menu = {
    1: {"item": "Veg Pizza", "price": 150},
    2: {"item": "Cheese Pizza", "price": 200},
    3: {"item": "Burger", "price": 100},
    4: {"item": "Coke", "price": 50},
    5: {"item": "Cheese Pizza with Coke", "price": 240},
    6: {"item": "Veg Pizza with Coke", "price": 190},
    7: {"item": "Burger with Coke", "price": 140},
    8: {"item": "Veg Pizza Burger and Coke", "price": 290},
    9: {"item": "Cheese Pizza with Burger and Coke", "price": 340},
}
# Initialize order and total bill
order = {}
total_bill = 0
# Display menu
print("\n--- Cafe Menu ---")
for key, item in menu.items():
    print(f"{key}. {item['item']}: ${item['price']}")
# Place order
while True:
    choice = input("\nEnter your choice (or '0' to finish ordering): ")
    if choice == '0':
        break
    elif choice.isdigit() and 1 <= int(choice) <= 9:
        choice = int(choice)
        quantity = int(input("Enter quantity: "))
        
        if choice in order:
            order[choice]["quantity"] += quantity
        else:
            order[choice] = {"item": menu[choice]["item"], "price": menu[choice]["price"], "quantity": quantity}
            
        print(f"Added {menu[choice]['item']} x {quantity} to order.")
    else:
        print("Invalid choice. Please try again.")

# Calculate and display bill
print("\n--- Your Order ---")
for key, item in order.items():
    subtotal = item["price"] * item["quantity"]
    total_bill += subtotal
    print(f"{item['item']}: {item['quantity']} x ${item['price']} = ${subtotal}")
    
print(f"\nTotal Bill: ${total_bill}")
print("\nThank you for ordering!")
