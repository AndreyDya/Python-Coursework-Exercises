# Initialize empty cart
shopping_cart = []
# Add items (with prices)
shopping_cart.append(("Apple", 500))
shopping_cart.append(("Bread", 2990))
shopping_cart.append(("Milk", 3490))
print(f"Cart has {len(shopping_cart)} items")
# Calculate total
total = 0
for item, price in shopping_cart:
    total += price
    print(f"{item}: {total:,.2f}")
